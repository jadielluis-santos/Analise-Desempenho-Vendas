# Análise de Desempenho de Vendas 2024

Projeto de portfólio de Análise de Dados e Business Intelligence: ETL em Python, análise exploratória e dashboard em Power BI sobre um ano de vendas de uma varejista de eletrônicos.

> **Dados fictícios.** A empresa ("ComercioTech"), os clientes, os produtos e os valores são sintéticos, criados para estudo. Nenhum número representa um cliente real.

**Papel:** Analista de Dados (projeto individual de estudo).

## Principais resultados (KPIs)

Base: 1.000 vendas de 01/01/2024 a 31/12/2024, 20 produtos, 50 clientes.

| Métrica | Valor | Leitura |
| :--- | :--- | :--- |
| **Receita total** | **R$ 12,11 milhões** | Faturamento do ano. |
| **Margem bruta global** | **24,62%** (R$ 2,98 milhões) | Lucratividade geral. |
| **Ticket médio** | **R$ 12.112,84** | Poucas vendas de alto valor. |
| **Vendas abaixo do custo** | **361 de 1.000 (36%)** | Somam R$ 2,27 milhões de prejuízo. É o principal alerta da base. |
| **Melhor categoria (margem)** | **Acessório (27,96%)** | Também a maior receita. |
| **Pior categoria (margem)** | **Notebook (18,53%)** | Margem baixa para o volume vendido. |
| **Meta anual de receita** | **R$ 4,93 milhões → 245,8% atingido** | Meta definida por mês, igual para todas as regiões. |
| **Mês de menor margem** | **Janeiro (7,7%)** | Dezembro vem em seguida (18,6%). |

## Stack

| Área | Ferramentas |
| :--- | :--- |
| **ETL e análise** | Python (Pandas, NumPy) |
| **Visualização (EDA)** | Matplotlib, Seaborn |
| **BI** | Power BI |
| **Previsão** | Regressão linear simples (NumPy) |
| **Versionamento** | Git/GitHub |

## Estrutura e pipeline

```
dados_brutos/        vendas, produtos, clientes, metas (CSV)
scripts/etl_dados.py limpeza, cálculo de receita/custo/margem e integração das bases
scripts/analise_exploratoria.ipynb  análise exploratória (EDA)
dados_processados/   dataset_final.csv
```

### ETL (`etl_dados.py`)
1. **Limpeza:** remoção de duplicados e tipagem de datas e IDs.
2. **Feature engineering:** `receita_liquida`, `custo_total` e `margem_bruta_total` por venda.
3. **Integração:** junção de vendas com produtos (`id_produto`), clientes (`id_cliente`) e metas (mês).

**Limitação conhecida:** o mês da venda é gerado em inglês (`Feb`, `Apr`...) e a base de metas usa português (`Fev`, `Abr`...). Por isso, 626 vendas de 7 meses (fev, abr, mai, ago, set, out e dez) ficam sem meta no `dataset_final.csv`. Os números de meta deste README foram calculados direto da base de metas, mês a mês.

## Insights da análise exploratória

### 1. Lucratividade por categoria

| Categoria | Receita | Margem bruta | Leitura |
| :--- | :--- | :--- | :--- |
| Acessório | R$ 5,61 mi | **27,96%** | Maior receita e maior margem. |
| Smartphone | R$ 2,93 mi | 25,64% | Margem saudável. |
| Notebook | R$ 3,58 mi | **18,53%** | **Alerta:** margem baixa; revisar custo de aquisição ou preço. |

- **Mais rentáveis:** Produto_13 (42,2%) e Produto_12 (40,9%).
- **Menos rentáveis:** Produto_10 (2,4%) e Produto_16 (8,3%).

### 2. Vendas abaixo do custo

Em **361 das 1.000 vendas** o custo unitário é maior que o preço de venda. Essas vendas somam **R$ 2,27 milhões de prejuízo**, o que derruba a margem global. Aparecem em todas as regiões (Sul é a que mais tem: 89) e em todas as categorias (Acessório: 152). Antes de qualquer meta, este é o ponto a investigar: erro de cadastro de custo, promoção mal precificada ou venda realmente deficitária.

### 3. Metas e desempenho regional

A base de metas tem **uma meta por mês**, igual para todas as regiões. Por isso não dá para medir atingimento por região, só no total.

- **Meta anual de receita:** R$ 4,93 milhões. **Realizado:** R$ 12,11 milhões (**245,8%**).
- Todos os meses superaram a meta; o menor atingimento foi em dezembro (149,8%) e março (150,9%).
- **Meta de lucro:** R$ 1,65 milhão. **Margem realizada:** R$ 2,98 milhões.

Comparação entre regiões (sem meta):

| Região | Receita | Margem bruta |
| :--- | :--- | :--- |
| Sul | R$ 2,65 mi | 26,2% |
| Centro-Oeste | R$ 2,52 mi | 25,2% |
| Norte | R$ 2,49 mi | **29,6%** (maior margem) |
| Sudeste | R$ 2,38 mi | 26,3% |
| Nordeste | R$ 2,08 mi | **14,0%** (menor margem; requer atenção) |

### 4. Perfil do cliente e sazonalidade

- **Público:** a faixa **26–35 anos** gera a maior receita (R$ 3,68 mi), seguida de perto por 46–60 (R$ 3,57 mi). O público **feminino** gera mais receita (R$ 6,34 mi contra R$ 5,78 mi).
- **Canal:** o **Site** lidera em receita (R$ 5,02 mi); o **Marketplace** tem a menor margem (19,7%).
- **Sazonalidade:** picos de receita em **maio** (R$ 1,26 mi) e **agosto** (R$ 1,19 mi). **Janeiro** tem a menor margem do ano (7,7%, R$ 70 mil); dezembro vem em seguida (18,6%).

### 5. Projeção de vendas

Uma regressão linear simples sobre a receita mensal de 2024 projeta:

| Mês (2025) | Receita prevista |
| :--- | :--- |
| Janeiro | R$ 985.107,09 |
| Fevereiro | R$ 981.369,20 |
| Março | R$ 977.631,31 |

**Leitura honesta:** o R² do modelo é 0,007, ou seja, a tendência linear praticamente não explica a variação entre os meses. A projeção serve só como referência de patamar (cerca de R$ 1 milhão por mês, igual à média de 2024). Para prever de verdade, o próximo passo é testar modelos com sazonalidade (Prophet) e mais de um ano de histórico.

## Dashboard

O dashboard interativo em Power BI está publicado na web, com KPIs, sazonalidade e comparação regional:

[Acessar o dashboard publicado](https://app.powerbi.com/view?r=eyJrIjoiNGJjMGM5NzktZjhlYy00MTY1LWJkOTYtM2RkYzM2ZjQyNzVlIiwidCI6ImIwZTczMzVmLWZkMWYtNDZhZC05OGM3LTU1ZTZlNGUyMjJlYSJ9)

## Próximos passos

1. Corrigir a junção de metas no ETL (padronizar o nome do mês).
2. Investigar as 361 vendas abaixo do custo e separar erro de cadastro de prejuízo real.
3. Testar previsão com sazonalidade (Prophet).

---

*Detalhes técnicos nos scripts da pasta `scripts/`.*
