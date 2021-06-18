
from pandas import DataFrame

def sma(df: DataFrame, span:int, column_name = 'sma') -> None:
    df[column_name] = df['close'].rolling(window=span).mean()

def ema(df: DataFrame, span:int, column_name = 'ema') -> None:
    df[column_name] = df['close'].ewm(span=span, adjust= False).mean()

def rma(df: DataFrame, span:int, column_name = 'rma') -> None:
    df[column_name] = df['close'].ewm(com=span-1, adjust= False).mean()    
            
