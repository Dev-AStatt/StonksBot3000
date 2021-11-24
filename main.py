#im sorry this has to be dt, i hate doing it but for some reason calling it datetime doesn't work?????
from datetime import datetime
import time
import matplotlib.pyplot as plt
from matplotlib import style
from pingAPI import *
from trades.tradeManager import *
from training.trainingAPI import *

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
#   pip         <- to install pandas
#   pandas      <- tool for importing and managing basically excel data
#   matplotlib  <- tool for displaying graphs and such things

#   References:
#   https://jamesgeorgedunn.com/2020/10/05/using-python-and-pandas-to-analyse-cryptocurrencies-with-coinapi/
#   https://pandas.pydata.org/getting_started.html



def main():
    #do not flag this as true unless you want to ping the API
    get_Historical_Data = False
    run_training_simulation = True
    display_graphs = True
    if(get_Historical_Data):
        api = CoinAPI__Interface()
        api.get_historical_data_and_save_csv("LTC/USD", "1HRS", "2020-01-01T00:00:00", "2021-10-31T23:59:00","100000")
        print("Sucsessful?")

    #testing feature of adding a trade and printing update
    trademan = tradeManager()
    #load training data
    training = training_API(True)
    if(display_graphs):
        #training.active_chart['Price Open'].plot()
        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
        ax1.plot(training.active_chart_1h.index, training.active_chart_1h['Price Open'])
        ax1.plot(training.active_chart_1h.index, training.active_chart_1h['100ta'])
        ax2.bar(training.active_chart_1h.index, training.active_chart_1h['Volume Traded'])
        plt.show()

    #Run training sumulation
    while(run_training_simulation):
        training.update_ticker_data("LTC/USD")
        time.sleep(1)
    #adding a new trade
    trademan.new_trade("LTC",0.1,6000,datetime.now())
    trademan.print_trades()

if __name__ == '__main__':
    main()

# Debug function if you ever need to print the whole database
#ltc_data.to_csv("DEBUG_History.csv", index = False)
#edit
