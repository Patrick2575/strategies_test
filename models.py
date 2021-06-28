from pandas import DataFrame

#---------------------------------------------------------------------------------------------------
#
# Order class
#---------------------------------------------------------------------------------------------------
class Order:
    def __init__(self, exec_time, type, amount, uprice) -> None:
        self._exec_time = exec_time
        self._type = type
        self._amount = amount
        self._uprice = uprice
        self._volume = 0
        self._value  = 0

        if self._type == 'sell':
            self._volume = amount
            self._value  = amount * uprice
        
        else:
            self._value  = amount
            self._volume = amount / uprice

    
    @property
    def exec_time(self) :
        return self._exec_time

    @property
    def is_buy(self) :
        return True if self._type == 'buy' else False

    @property
    def volume(self) :
        return self._volume

    @property 
    def uprice(self) :
        return self._uprice

    @property
    def value(self) :
        return self._value

    def as_array(self):
        '''
        returns the order as an array  [is_buy, volume, price, value]
        buy is true for a buy order, otherwise False
        '''
        return [self.exec_time, self.is_buy, self.volume, self.uprice, self.value]
            
#---------------------------------------------------------------------------------------------------
#
# Wallet class
#---------------------------------------------------------------------------------------------------
class Wallet:
    def __init__(self, base_assets, quote_assets) -> None:
        self._base_assets = base_assets
        self._quote_assets = quote_assets
        self._orders = []

    #---------------------------------------------------------------------------------
    def sell(self, price, exec_time):
        if self._base_assets <= 0:
            print('Could not sell no base assets available')
            return

        order =  Order(exec_time, 'sell', self._base_assets, price )
        self._base_assets = 0.0
        self._quote_assets = order._value
        self._orders.append(order)

    #---------------------------------------------------------------------------------
    def buy(self, price, exec_time):
        if self._quote_assets <= 0:
            print('Could not buy no quote assets available')
            return
        
        order =  Order(exec_time, 'buy', self._quote_assets, price )
        self._base_assets  = order._volume
        self._quote_assets = 0.0
        self._orders.append(order)


    def orders_as_dataframe(self):
        orders = []
        for order in self._orders:
            orders.append(order.as_array())

        df = DataFrame(orders)
        df.columns = ['time', 'buy', 'volume', 'price', 'value']
        return df
