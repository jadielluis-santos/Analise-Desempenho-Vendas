# Análise de Desempenho de Vendas 2024 - ComercioTech

## Introdução
Este projeto é uma Análise de Dados e Business Intelligence (BI) completa, realizada para a varejista nacional ComercioTech, especializada em produtos eletrônicos e de informática. O objetivo é fornecer uma visão executiva do desempenho de vendas e lucratividade em 2024, identificando tendências, anomalias e oportunidades.

**Papel:** Analista de Dados / Cientista de Dados Júnior.

## Principais Resultados Executivos (KPIs)

| Métrica | Valor | Insights Chave |
| :--- | :--- | :--- |
| **Receita Total** | **R$ 12.11 Milhões** | Faturamento consolidado no período. |
| **Margem Bruta Global** | **24.62%** | Lucratividade geral do negócio. |
| **Ticket Médio** | **R$ 12,112.84** | Indica foco em vendas de Alto Valor/Baixo Volume. |
| **Melhor Categoria (Margem)** | **Acessórios (27.96%)** | Categoria mais rentável. |
| **Pior Categoria (Margem)** | **Notebooks (18.53%)** | Margem crítica, exige investigação de custos/preços. |
| **Melhor Região** | **Sul (141.44% Atingimento)** | Líder absoluta em superação de metas de receita. |
| **Alerta (Sazonalidade)**| **Dezembro** | Mês com a menor margem bruta, atípico para o varejo. |

## Stack Tecnológica

| Área | Ferramentas/Bibliotecas |
| :--- | :--- |
| **ETL e Análise** | Python (Pandas, NumPy) |
| **Visualização (EDA)** | Python (Matplotlib, Seaborn) |
| **Versionamento** | Git/GitHub |
| **BI (Recomendado)** | Power BI / Looker Studio |
| **Previsão (Próxima Fase)** | Prophet / Scikit-learn |

## Estrutura do Projeto e Pipeline

O projeto segue um pipeline modularizado e reprodutível:

### Detalhes do ETL (`etl_dados.py`)
1.  **Limpeza:** Tratamento de valores nulos e tipagem de colunas (datas e IDs).
2.  **Feature Engineering:** Cálculo de `Receita Líquida`, `Custo Total` e `Margem Bruta Total` por transação.
3.  **Integração (Joins):** Unificação das 4 bases por `id_produto`, `id_cliente` e `mês/região`.

## Insights Detalhados da Análise Exploratória (EDA)

### 1. Análise de Lucratividade

| Categoria | Receita Total | Margem Bruta % | Recomendação Estratégica |
| :--- | :--- | :--- | :--- |
| Acessório | R$ 5.60M | **27.96%** | Categoria de maior volume e rentabilidade. Manter a estratégia. |
| Smartphone | R$ 2.92M | 25.64% | Boa margem, maior Ticket Médio. Explorar oportunidades de *upsell*. |
| Notebook | R$ 3.57M | **18.53%** | **ALERTA!** Margem de lucro muito baixa para o volume de receita. Sugerimos investigação imediata do custo de aquisição ou ajuste de preço de venda. |

**Top Rentáveis:** Os produtos `Produto_13` e `Produto_12` apresentaram as maiores margens (acima de $40\%$).

### 2. Atingimento de Metas e Desempenho Regional

Todas as regiões superaram a meta de receita consolidada (Meta Total: R\$ 1.94M / Receita Realizada: R\$ 12.11M).

| Região | Atingimento Total % | Ranking |
| :--- | :--- | :--- |
| **Sul** | **141.44%** | **1º** (Analisar fatores de sucesso para replicar) |
| Centro-Oeste | 129.63% | 2º |
| Norte | 128.11% | 3º |
| Sudeste | 122.58% | 4º |
| Nordeste | **106.98%** | **5º** (Requer atenção por ter o menor desempenho, apesar de ter superado a meta). |

### 3. Perfil do Cliente e Sazonalidade

* **Público-Alvo:** A maior fatia da receita vem da faixa etária **26-35 anos** e o público **Feminino** gera a maior receita total.
* **Sazonalidade:** Vendas atingiram picos em **Maio e Agosto**. Dezembro é o mês com a menor margem absoluta (R\$ 149K), o que é uma anomalia para o setor e deve ser investigada.

## Próximos Passos (BI e Previsão)

Com este dataset consolidado, a próxima fase do projeto envolve:

1.  **Dashboard Executivo (BI):** Criação de um dashboard interativo (Power BI/Looker Studio) para acompanhar os KPIs de Receita, Margem, Top Produtos e Atingimento de Metas por Região em tempo real.

   ## 📊 VISUALIZAÇÃO DO DASHBOARD EXECUTIVO

O Dashboard interativo do Power BI foi publicado na Web, permitindo a exploração dinâmica dos KPIs, Sazonalidade e Ranking Regional.

Acesse o **Dashboard Interativo** para explorar os resultados ao vivo:

[ACESSE O DASHBOARD PUBLICADO AQUI](https://app.powerbi.com/view?r=eyJrIjoiNGJjMGM5NzktZjhlYy00MTY1LWJkOTYtM2RkYzM2ZjQyNzVlIiwidCI6ImIwZTczMzVmLWZkMWYtNDZhZC05OGM3LTU1ZTZlNGUyMjJlYSJ9)


2.  **Previsão de Vendas:** Aplicação do modelo de séries temporais (Prophet) para prever a receita dos próximos 3 a 6 meses.### 4. Projeção de Vendas (Insights Avançados - ML)

Para atender à demanda por previsões, aplicamos uma Regressão Linear Simples aos dados de receita mensal (Jan-Dez 2024).

| Mês (2025) | Receita Prevista (R$) |
| :--- | :--- |
| **Janeiro** | R$ 985.107,09 |
| **Fevereiro** | R$ 981.369,20 |
| **Março** | R$ 977.631,31 |

**Conclusão do ML:** O modelo projeta uma estabilidade no patamar de R$ 980 mil/mês no início de 2025, sugerindo que a equipe comercial precisará de ações estratégicas (e não apenas do impulso sazonal) para ultrapassar a marca de R$ 1 milhão.


***

*Para mais detalhes técnicos, consulte os scripts na pasta `scripts/`.*


