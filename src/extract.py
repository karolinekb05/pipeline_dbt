# imports
import pandas as pd
import yfinance as yf

commodities = ['CL=F', 'GC=F', 'SI=F']

# ingerir a cotação dos ativos
def ingest_data(ticker, period='5d', interval='1d'):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['ticker'] = ticker
    return data

# função que concatena os ativos
def union_data(data):
    all_data = []
    for ticker in commodities:
        data_append = ingest_data(ticker)
        all_data.append(data_append)
    return pd.concat(all_data)

if __name__ == '__main__':
    data_concat = union_data(commodities)
    print(data_concat)
