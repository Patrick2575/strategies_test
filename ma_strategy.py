from datetime import datetime
from models import Wallet
from pandas import DataFrame
from ohlcv_data import load_binance_data
from indicators import sma, ema, rma

def run_ma_strategy(df:DataFrame, ma:str = 'sma', span = 7) -> None:
    '''
    ma can be one of [sma, ema, 'rma]
    '''
    wallet = Wallet(0, 1000) 

    if ma == 'sma':
        sma(df=df, span=span, column_name=ma)
    elif ma == 'ema':
        ema(df=df, span=span, column_name=ma)
    elif ma == 'rma':
        rma(df=df, span=span, column_name=ma)
        
    else:
        print(f"unkown mouving average 'ma = {ma}' ")
        return

    for i in range(span +1, df.shape[0]):
        pi = i -1
        if df['close'][i] > df[ma][i] and df['close'][pi] <= df[ma][pi]:
            wallet.buy(df['close'][i])

        if df['close'][i] < df[ma][i] and df['close'][pi] >= df[ma][pi]:
            wallet.sell(df['close'][i])

    last_row = df.shape[0] - 1
    wallet.sell(df['close'][last_row])
    print(f'{len(wallet._orders)} order(s) executed')
    print(f'base assets: {wallet._base_assets}')
    print(f'quote assets: {wallet._quote_assets}')

    print('--- vs ---')
    wallet = Wallet(0, 1000)
    wallet.buy(df['close'][0])
    wallet.sell(df['close'][last_row])
    print(f'quote assets: {wallet._quote_assets}')


# --- test function
symbol = 'BTC/USDT'
candel_interval = '1h'
since = int(datetime.timestamp(datetime.strptime('01/01/2021', '%d/%m/%Y')) * 1000)
span = 7
df = load_binance_data(symbol, candel_interval, since=since)
print(f'------------------------------SMA {candel_interval}------------------------------------------')
ma_name = 'sma'
run_ma_strategy(df, ma = ma_name, span= span)

print(f'------------------------------EMA {candel_interval}------------------------------------------')
ma_name = 'ema'
run_ma_strategy(df, ma = ma_name, span= span)

print(f'------------------------------RMA {candel_interval}------------------------------------------')
ma_name = 'rma'
run_ma_strategy(df, ma = ma_name, span= span)