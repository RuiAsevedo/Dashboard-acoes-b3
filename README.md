# Dashboard de Análise de Ações da B3 (Terminal BI)

Este projeto é uma ferramenta de Business Intelligence e Análise de Dados desenvolvida em Python para extração, processamento e visualização de métricas de ativos da bolsa brasileira (B3).

O script automatiza o fluxo de ETL (Extração, Transformação e Carga), substituindo a coleta manual por uma análise programática direta no terminal.

## Objetivo do Projeto
Demonstrar a aplicação de lógica de programação na resolução de problemas do mercado financeiro, construindo um pipeline de dados capaz de gerar *insights* rápidos para tomada de decisão.

## Tecnologias Utilizadas
- **Python 3:** Linguagem principal.
- **yfinance:** Extração de dados reais e atualizados do mercado financeiro (API do Yahoo Finance).
- **pandas:** Manipulação de DataFrames e cálculo de indicadores (KPIs).

## Funcionalidades (Pipeline de Dados)
1. **Extração (Data Extraction):** O usuário inputa o *ticker* da ação (ex: `ITUB4.SA`, `PETR4.SA`) e o script coleta o histórico de cotações do último ano.
2. **Transformação (Data Transformation):** O motor calcula KPIs essenciais para o mercado financeiro:
- Preço de Fechamento Atual.
- Retorno Percentual (ROI) no período de 1 ano.
- Volatilidade e limites operacionais (Máxima e Mínima do período).
3. **Visualização (Data Visualization):** Geração de um "Dashboard Executivo" em formato de texto no terminal, acompanhado de uma regra condicional simples que gera um insight automático sobre a valorização ou desvalorização do ativo.

## Como Executar
Para rodar este projeto na sua máquina, certifique-se de ter o Python instalado e siga os passos:

1. Clone este repositório:
`git clone https://github.com/RuiAsevedo/dashboard-acoes-b3.git`

2. Instale as dependências necessárias:
`pip install pandas yfinance`

3. Execute o script no terminal:
`python3 analise_b3.py`

---
*Desenvolvido por Rui Charles Asevedo Chaves - Analista de TI focado em Dados & Automação.*

