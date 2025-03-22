# imports
import pandas as pd
import yfinance as yf

commodities = ['CL=F', 'GC=F', 'SI=F']

# ingerir a cotação dos ativos
def ingest_data(ticker, period='5d', interval='1d'):
    ticker_obj = yf.Ticker(ticker)
    data = ticker_obj.history(period=period, interval=interval)[['Close']]
    data['ticker'] = ticker  # Salvar apenas o símbolo do ticker
    return data

# função que concatena os ativos
def union_data(data):
    all_data = []
    for ticker in commodities:
        data_append = ingest_data(ticker)
        all_data.append(data_append)
    return pd.concat(all_data)

# Criar a variável data_concat que será importada por outros módulos
data_concat = union_data(commodities)

if __name__ == '__main__':
    print(data_concat)
