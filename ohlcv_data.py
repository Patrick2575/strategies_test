import ccxt, os
import pandas as pd

def load_binance_data(symbol, candel_interval, since = None,  from_cache = True) -> pd.DataFrame:
    current_file_folder = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(current_file_folder, 'data')
    clean_symbol = symbol.replace('/', '')
    since_str = f'_since{since}' if since else ''
    cache_csv_file = os.path.join(data_folder, f'binance_ohlcv_{clean_symbol}_{candel_interval}{since_str}.csv')

    if from_cache and os.path.exists(cache_csv_file):
        print(' Loading data from cache ...')
        df = pd.read_csv(cache_csv_file)
        return df
    
    print(' Loading data from binance ...')
    binance = ccxt.binance()
    ohlcvc_data = binance.fetch_ohlcv(symbol=symbol, timeframe=candel_interval, since=since)
    df = pd.DataFrame(ohlcvc_data)
    df.columns = ['time', 'open','high', 'low','close','volume']

    # save data into cache
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    df.to_csv(cache_csv_file, index=False)
    print(' Cache updated')
    return df

# -- test the function
'''
from datetime import datetime
symbol = 'BTC/USDT'
candel_interval = '1h'
since = int(datetime.timestamp(datetime.strptime('16/06/2021', '%d/%m/%Y')) * 1000)
df = load_binance_data(symbol, candel_interval, since=since)
print(df)
'''

