#im sorry this has to be dt, i hate doing it but for some reason calling it datetime doesn't work?????
from datetime import datetime
from pingAPI import *
from trades.tradeManager import *
from util.table_import_refactor import *

#-----------------------------------------------------------------------------------------------------------#
#                                   StonkBot3000                                                            #
#               Created by Aaron Statt, Trey Chambers, and Benito Tijerina                                  #
#                                                                                                           #
#   we have setup an API link to CoinAPI.io that compiles multiple exchanges and can return alot of         #
#   coin data.  The API is free for hobby projects but only allows 100 queries per day.                     #
#   For training we can export the queried data to a csv file, then read it over and over while testing.    #
#                                                                                                           #
#   The following code uses a pre-existing csv file (That is in the git dir)                                #
#                                                                                                           #
#-----------------------------------------------------------------------------------------------------------#

#   Required installs
#   pip     <- to install pandas
#   pandas  <- tool for importing and managing basically excel data

#   References:
#   https://jamesgeorgedunn.com/2020/10/05/using-python-and-pandas-to-analyse-cryptocurrencies-with-coinapi/
#   https://pandas.pydata.org/getting_started.html



def main():
    #do not flag this as true unless you want to ping the API
    get_Historical_Data = False

    if(get_Historical_Data):
        api = CoinAPI__Interface()
        api.get_historical_data_and_save_csv("LTC/USD", "1HRS", "2020-01-01T00:00:00", "2021-10-31T23:59:00","100000")
        print("Sucsessful?")


    #ltc_data is a panda data structure that is kinda like an excel sheet
    ltc_data = pandas.read_csv("History_FromAPI.csv")

    ltc_data = refactorData(ltc_data)

    #this will print the first 5 enteries of the structure. Use .tail() to get the last 5
    print(ltc_data.head())

    #testing feature of adding a trade and printing update
    trademan = tradeManager()
    #adding a new trade
    trademan.new_trade("BTC",0.1,6000,datetime.now())
    trademan.print_trades()

if __name__ == '__main__':
    main()

# Debug function if you ever need to print the whole database
#ltc_data.to_csv("DEBUG_History.csv", index = False)
#edit
