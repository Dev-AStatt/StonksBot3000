#_Trade Class

#
# Hold a single trade instance, position and goal
#

class trade:
    def __init__(self,coin_ticker, bought_price, amount, date):
        self._coin_ticker = coin_ticker
        self._bought_price = bought_price
        self._amount = amount
        self._date_bought = date

    def get_ticker(self):
        return self._coin_ticker
    
    def get_bought_price(self):
        return self._bought_price
    
    def get_amount(self):
        return self._amount

    # Will print out the current class to the terminal
    def print_trade(self):
        amount_string = str(self._amount)
        price_string = str(self._bought_price)
        print("Coin: " + self._coin_ticker + ", date: " + self._date_bought.strftime("%y/%m/%d") + ", amount: " + amount_string + ", Price: " + price_string)
