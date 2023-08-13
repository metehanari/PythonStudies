# API

import pandas as pd
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

print(bitcoin_data)


data = pd.DataFrame(bitcoin_data, columns=['TimeStamp', 'Price'])

print(data)