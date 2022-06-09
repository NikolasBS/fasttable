import requests
import pandas as pd
import json
from fastapi.responses import JSONResponse
from model import trading_pairs_table

class Table():
    def JSONTable():

        r = requests.get('https://api.binance.com/api/v3/ticker/24hr')
        j = json.loads(r.text)


        df = pd.DataFrame(j, columns=["symbol", "priceChangePercent", "lastPrice" , "volume", "weightedAvgPrice"])

        df['lastPrice'] = pd.to_numeric(df['lastPrice'])
        df['weightedAvgPrice'] = pd.to_numeric(df['weightedAvgPrice'])
        df['priceChangePercent'] = pd.to_numeric(df['priceChangePercent'])


        # Filtra os tokens USDT
        search = "USDT"
        bool_series = df['symbol'].str.endswith(search)

        check = df[bool_series]


        # Extração de todos os tokens
        symbol = df['symbol']

        # Criação de lista com sufixos a serem eliminados
        exclude = ['UP', 'DOWN', 'BEAR', 'BULL']

        # Criação de lista com tokens a serem eliminados 
        irrelevant = [symbol for symbol in symbol if all(excludes not in symbol for excludes in exclude)]

        # Criação de lista com tokens a serem mantidos (sufixo USDT)
        relevant = [symbol for symbol in irrelevant if symbol.endswith('USDT')]

        check.sort_values(by=['priceChangePercent'], ascending=False)
        js = check.to_json()
        y = json.loads(js)

        return y