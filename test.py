API_KEY = 'PKREKYW9OZ6NZFNN8S8Z'
SECRET_KEY = '8wF9YNrUWdOcABnBV6ltyjzNiLaArZEMTbfavloo'

from alpaca.data.live import StockDataStream
ds = StockDataStream(API_KEY, SECRET_KEY)

async def bar_callback(bar):
    for property_name, value in bar:
        print(f"\"{property_name}\": {value}")
        

sym = 'SPY'
ds.subscribe_bars(bar_callback, sym)
ds.run()