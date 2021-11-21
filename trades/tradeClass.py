#Trade Class

#
# Hold a single trade instance, position and goal
#

class trade:
    def _init_(self,coin_ticker, bought_price, amount):
        self._coin_ticker = coin_ticker
        self._bought_price = bought_price
        self._amount = amount

    def get_ticker():
        return self._coin_ticker
    
    def get_bought_price():
        return self._bought_price
    
    def get_amount():
        return self._amount

