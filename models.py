#---------------------------------------------------------------------------------------------------
#
# Order class
#---------------------------------------------------------------------------------------------------
class Order:
    def __init__(self, type, amount, uprice) -> None:
        self._type = type
        self._amount = amount
        self._uprice = uprice
        self._volume = 0
        self._value  = 0

        if self._type == 'sell':
            self._value = amount * uprice
        
        else:
            self._volume = amount / uprice
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
    def sell(self, price):
        if self._base_assets <= 0:
            print('Could not sell no base assets available')
            return

        order =  Order('sell', self._base_assets, price )
        self._base_assets = 0.0
        self._quote_assets = order._value
        self._orders.append(order)

    #---------------------------------------------------------------------------------
    def buy(self, price):
        if self._quote_assets <= 0:
            print('Could not buy no quote assets available')
            return
        
        order =  Order('buy', self._quote_assets, price )
        self._base_assets  = order._volume
        self._quote_assets = 0.0
        self._orders.append(order)
