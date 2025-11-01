import pandas as pd
import numpy as np
import os
import sys
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE CAMINHOS ---
# Caminhos relativos para a leitura e escrita
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
DADOS_BRUTOS_PATH = os.path.join(BASE_DIR, '..', 'dados_brutos')
DADOS_PROCESSADOS_PATH = os.path.join(BASE_DIR, '..', 'dados_processados')

# Garante que o diretório de saída exista
os.makedirs(DADOS_PROCESSADOS_PATH, exist_ok=True)

print("\n--- 1. CARREGAMENTO DOS DADOS REAIS ---")

# Leitura dos arquivos CSV
try:
    # Lendo os 4 arquivos da pasta dados_brutos
    df_vendas = pd.read_csv(os.path.join(DADOS_BRUTOS_PATH, 'vendas.csv')) 
    df_produtos = pd.read_csv(os.path.join(DADOS_BRUTOS_PATH, 'produtos.csv')) 
    df_clientes = pd.read_csv(os.path.join(DADOS_BRUTOS_PATH, 'clientes.csv')) 
    df_meta = pd.read_csv(os.path.join(DADOS_BRUTOS_PATH, 'meta_vendas.csv')) 
except FileNotFoundError as e:
    print(f"ERRO: Arquivo não encontrado. Verifique se os 4 CSVs estão em {DADOS_BRUTOS_PATH}. Detalhe: {e}")
    sys.exit() 

print(f"Vendas carregadas: {len(df_vendas)} linhas.")
print(f"Produtos carregados: {len(df_produtos)} linhas.")
print(f"Clientes carregados: {len(df_clientes)} linhas.")
print(f"Metas carregadas: {len(df_meta)} linhas.")


# --- 2. LIMPEZA E PREPARAÇÃO (Transform) ---

# Tabela Vendas
print("\nProcessando Vendas...")
df_vendas.drop_duplicates(inplace=True)
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'], errors='coerce') 
df_vendas['id_cliente'] = df_vendas['id_cliente'].astype(str)

# Criação de Features Financeiras (Receita, Custo e Margem)
df_vendas['receita_liquida'] = df_vendas['quantidade'] * df_vendas['preco_unitario'] 
df_vendas['custo_total'] = df_vendas['quantidade'] * df_vendas['custo_unitario'] 
df_vendas['margem_bruta_total'] = df_vendas['receita_liquida'] - df_vendas['custo_total']

# Criação de Chave Temporal (Mês e Ano/Mês)
df_vendas['mes_nome'] = df_vendas['data_venda'].dt.strftime('%b').str.title() 
df_vendas['ano_mes'] = df_vendas['data_venda'].dt.to_period('M').dt.to_timestamp()


# Tabela Produtos
print("Processando Produtos...")
df_produtos.drop_duplicates(inplace=True)
df_produtos.rename(columns={'id_produto': 'id_prod_ref', 
                            'categoria': 'categoria_produto',
                            'marca': 'marca_produto'}, inplace=True) 

# Tabela Clientes
print("Processando Clientes...")
df_clientes.drop_duplicates(inplace=True)
df_clientes.rename(columns={'estado': 'estado_cliente',
                            'genero': 'genero_cliente'}, inplace=True) 
df_clientes['id_cliente'] = df_clientes['id_cliente'].astype(str)


# Tabela Metas
print("Processando Metas...")
df_meta.rename(columns={'mes': 'mes_nome'}, inplace=True) 
df_meta['mes_nome'] = df_meta['mes_nome'].str.title()
df_meta.drop_duplicates(subset=['mes_nome'], keep='first', inplace=True)

# Cria KPI de margem percentual alvo
df_meta['meta_margem'] = (df_meta['meta_lucro'] / df_meta['meta_receita']) * 100 
df_meta.drop(columns=['meta_lucro'], inplace=True) 


# --- 3. INTEGRAÇÃO (MERGE) ---
print("\nIntegrando bases de dados (Joins SQL-like)...")

# Merge 1: Vendas + Produtos
df_merged = pd.merge(
    df_vendas, 
    df_produtos, 
    left_on='id_produto', 
    right_on='id_prod_ref', 
    how='left'
)

# Merge 2: Resultado + Clientes
df_merged = pd.merge(
    df_merged, 
    df_clientes.drop(columns=['nome_cliente']), 
    on='id_cliente', 
    how='left'
)

# Tratamento de Nulos pós-Merge Cliente
df_merged['genero_cliente'].fillna('Não Cadastrado', inplace=True) 
df_merged['faixa_etaria'].fillna('Não Cadastrada', inplace=True)
df_merged['estado_cliente'].fillna('Desconhecido', inplace=True)

# Merge 3: Resultado + Metas
df_final = pd.merge(
    df_merged,
    df_meta,
    on='mes_nome',
    how='left'
)
print(f"Dataset Final criado com: {len(df_final)} linhas.")

# --- 4. SALVAR O DATASET PROCESSADO ---
output_file = os.path.join(DADOS_PROCESSADOS_PATH, 'dataset_final.csv')
df_final.to_csv(output_file, index=False)

print("\n--- SUCESSO: ETL CONCLUÍDO ---")
print(f"Dataset final salvo em: {output_file}")