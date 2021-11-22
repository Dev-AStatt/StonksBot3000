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
        self._exchange = "NA"
        self._exchange_fee = self.calc_exchange_fees()
        self._break_even_sell_price = self._amount + (self._amount * self._exchange_fee)

    #Standards for trades that need to be modular later
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
        break_even_str = str(self._break_even_sell_price)
        print("Coin: " + self._coin_ticker + ", date: " + self._date_bought.strftime("%y/%m/%d") + ", amount: $" + amount_string + ", Price: $" + price_string + ", break even: $" + break_even_str)

    #calculate exchange fees for trade, will return the exchange fee %
    def calc_exchange_fees(self):
        # randomly selecting trading fee worst case from Kracken
        # https://support.kraken.com/hc/en-us/articles/201893638
        return 0.26 #this is 0.26%
  
