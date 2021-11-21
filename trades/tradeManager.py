from trades.tradeClass import *

#Trade Manager Class
#
#Trade Manager Class used to hold all of the active trades at once
#



class tradeManager:
    _allTrades = []

    def _init_(self):
        #add instatiation crap here
        print("Something had to go here")
    
    def new_trade(self,tracker,bought,amount ):
        #add new trade to list
        self._allTrades.append(trade(tracker,bought,amount))

