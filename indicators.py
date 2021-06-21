
from pandas import DataFrame
from ta.trend import SMAIndicator
from ta.trend import EMAIndicator
from ta.trend import WMAIndicator

def sma(df: DataFrame, span:int, column_name = 'sma') -> None:
    df[column_name] = SMAIndicator(close=df['close'], window= span).sma_indicator()

def ema(df: DataFrame, span:int, column_name = 'ema') -> None:
    df[column_name] =  EMAIndicator(close=df['close'], window= span).ema_indicator()

def wma(df: DataFrame, span:int, column_name = 'rma') -> None:
    df[column_name] = df['ta_rma'] =  WMAIndicator(close=df['close'], window= span).wma() 


# test
'''
from datetime import datetime
from ohlcv_data import load_binance_data
symbol = 'BTC/USDT'
candel_interval = '1h'
since = int(datetime.timestamp(datetime.strptime('01/01/2021', '%d/%m/%Y')) * 1000)
df = load_binance_data(symbol, candel_interval, since=since)
span = 50;
sma(df=df, span=span)
ema(df=df, span=span)
wma(df=df, span=span)

df.to_csv('out.csv')
print('saved')
'''
            
