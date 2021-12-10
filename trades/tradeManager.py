from trades.tradeClass import *
from util.supported_coins import *
#Trade Manager Class
#
#Trade Manager Class used to hold all of the active trades at once
#

class tradeManager:
    _allTrades = []

        #add instatiation crap here
    
    def new_trade(self, tracker, bought,amount, date):
        #add new trade to list
        self._allTrades.append(trade(tracker,bought,amount,date))

    # Will print all active trades if given no input
    # or can pass in the ticker string you want printed
    def print_trades(self, ticker = "ALL"):
        if not self._allTrades:  #if array is empty
            return          #just dont do anything
        if(ticker != "ALL"):
            for i in self._allTrades:
            #loop through array to match trades 
                if(self._allTrades[i].get_ticker() == ticker):
                    self._allTrades[i].print_trade() 
        #print out all active trades
        else:
            for trade in self._allTrades:
                trade.print_trade()




class Active_Dataframe:
    df_active_chart_1h = []

    def update_active_charts(self, symbol, new_df_row):
        """function accepts a new row of dataframe from api and appends it to active data charts"""
        if(symbol =  
