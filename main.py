import requests
import pandas as pd
import time
import datetime

headers = {"x-cg-demo-api-key": "SUACHAVE"}
criptos =["bitcoin", "ethereum", "solana", "render-token", "pendle", "immutable-x"]
params ={
    "vs_currency" : "usd",
    "days" : 365


lista_de_tabelas = []
for cripto in criptos:

    print(cripto)
    
    url = f"https://api.coingecko.com/api/v3/coins/{cripto}/market_chart"
    requisicao = requests.get(url, params = params, headers = headers)
    dados = requisicao.json()
    df_price = pd.DataFrame(dados["prices"], columns = ["data", "price"])
    df_volume = pd.DataFrame(dados["total_volumes"], columns = ["data", "volume"])
    df_final = df_price.merge(df_volume, on = 'data')
    df_final ["data"] = pd.to_datetime(df_final["data"], unit = "ms")
    df_final["cripto"] = cripto
    lista_de_tabelas.append(df_final)

dados_historicos = pd.concat(lista_de_tabelas)
dados_historicos

dados_historicos["cripto"].unique()

# Dados OHLC

params ={
    "vs_currency" : "usd",
    "days": 90

}

lista_de_tabelas = []


for cripto in criptos:

    print(cripto)
    
    url = f"https://api.coingecko.com/api/v3/coins/{cripto}/ohlc"
    requisicao = requests.get(url, params = params, headers = headers)
    dados = requisicao.json()
    df_ohlc = pd.DataFrame(dados, columns = ["data", "open", "high", "low", "close"])
    df_ohlc["data"] = pd.to_datetime(df_final["data"], unit = "ms")
    df_ohlc["cripto"] = cripto
    lista_de_tabelas.append(df_ohlc)

dados_ohlc = pd.concat(lista_de_tabelas)
print(dados_ohlc)

# dados_ohlc.to_csv("dados_cripto.csv") Para salvar em csv
# dados_ohlc.to_excel("dados_cripto.xlsx") Para salvar em excel
