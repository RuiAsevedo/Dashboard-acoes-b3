import yfinance as yf
import pandas as pd

def analisar_acao(ticker):
    print(f"\nIniciando a Extração de Dados para: {ticker}")
    print("-" * 50)

    # 1. EXTRAÇÃO: Baixando dados do último 1 ano
    acao = yf.Ticker(ticker)
    dados = acao.history(period="1y")

    # 2. TRANSFORMAÇÃO: Calculando KPIs
    preco_atual = dados['Close'].iloc[-1]
    preco_inicial = dados['Close'].iloc[0]
    retorno_percentual = ((preco_atual - preco_inicial) / preco_inicial) * 100

    preco_maximo = dados['High'].max()
    preco_minimo = dados['Low'].min()

    # 3. VISUALIZAÇÃO: Dashboard no Terminal
    print("DADOS PROCESSADOS COM SUCESSO! AQUI ESTÁ O SEU DASHBOARD:")
    print("-" * 50)
    print(f"Preco Atual (Fechamento): R$ {preco_atual:.2f}")
    print(f"Retorno no ultimo ano: {retorno_percentual:.2f}%")
    print(f"Maxima no periodo: R$ {preco_maximo:.2f}")
    print(f"Minima no periodo: R$ {preco_minimo:.2f}")
    print("-" * 50)

    # Insight simples
    if retorno_percentual > 0:
        print("INSIGHT: A acao apresentou valorizacao no periodo analisado.")
    else:
        print("INSIGHT: A acao sofreu desvalorizacao no periodo analisado.")


if __name__ == "__main__":
    acao_escolhida = input("Digite o codigo da acao (ex: PETR4.SA, VALE3.SA, ITUB4.SA): ")
    analisar_acao(acao_escolhida.upper())
