# Analisador de Ativos da B3 (Terminal BI)

Script em Python desenvolvido para extração, processamento e cálculo de KPIs financeiros de ativos listados na B3. O projeto atua como um pipeline simplificado de ETL, automatizando a coleta de dados de mercado e gerando um sumário executivo no terminal.

## Tecnologias e Bibliotecas
- Python 3.x
- yfinance (Integração de dados de mercado)
- pandas (Manipulação e transformação de DataFrames)

## Arquitetura do Script
A aplicação é dividida em três etapas principais:

1. **Coleta de Dados:** Utiliza a biblioteca `yfinance` para instanciar o objeto Ticker e extrair o histórico de preços (OHLC) do último 1 ano.
2. **Transformação e Cálculo de KPIs:** Utiliza métodos do `pandas` (como `.iloc`, `.max()`, `.min()`) para calcular:
- Preço de fechamento atual e inicial do período.
- Retorno percentual anualizado.
- Volatilidade bruta (Máxima e Mínima do período).
3. **Output:** Formatação dos dados estruturados em uma interface baseada em texto (CLI), incluindo uma verificação condicional básica para determinar a direção da tendência do ativo.

## Instruções de Execução

Requisitos prévios: Python 3 e gerenciador de pacotes pip instalados.

1. Clone o repositório:
`git clone https://github.com/RuiAsevedo/dashboard-acoes-b3.git`

2. Instale as dependências:
`pip install -r requirements.txt` *(ou utilize `pip install pandas yfinance`)*

3. Execute a aplicação:
`python3 analise_b3.py`

O script solicitará a entrada do ticker (ex: ITUB4.SA) e imprimirá a análise processada no terminal.

---
*Autor: Rui Asevedo - Analista de Dados / Automação*


