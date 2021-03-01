import finnhub
import pandas as pd
import time
import math

key = 'brkahqfrh5r9g3otl3g0'

# Setup client
finnhub_client = finnhub.Client(api_key=key)

# Stock candles
res = finnhub_client.stock_candles('AAPL', 'D', math.floor(time.time()-31536000), math.floor(time.time()))
print(pd.DataFrame(res))



