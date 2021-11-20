#im sorry this has to be dt, i hate doing it but for some reason calling it datetime doesn't work?????
import datetime as dt
from pingAPI import *

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


def number_to_day(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[number]

# method will take in the data structure, do generaic table management to make the table more
# usable and then return it. 
def refactorData(data):
    data.rename(columns = {
        "time_period_start": "Start Time",
        "time_period_end": "End Time",
        "time_open": "Open Time",
        "time_close": "Close Time",
        "price_open": "Price Open",
        "price_high": "Price High",
        "price_low": "Price Low",
        "price_close": "Price Close",
        "volume_traded": "Volume Traded",
        "trades_count": "Trade Count",
    }, inplace = True)

    # Drop columns of data we dont need
    ltc_data.drop(["End Time", "Open Time", "Close Time"], axis = "columns", inplace = True)

    # Convert the Start Time to a date/time data type
    ltc_data["Start Time"] = pandas.to_datetime(ltc_data["Start Time"])
    
    #add column for day of the week, filling it with the day of the week that column Start Time is
    ltc_data["Day of the Week"] = ltc_data['Start Time'].dt.dayofweek
    
    #change intager day of the week to string, just for visualization 
    ltc_data["Day of the Week"] = ltc_data["Day of the Week"].apply(number_to_day)

    return data

#ltc_data is a panda data structure that is kinda like an excel sheet
ltc_data = pandas.read_csv("LTC_Day_History_FromAPI.csv")

ltc_data = refactorData(ltc_data)

#this will print the first 5 enteries of the structure. Use .tail() to get the last 5
print(ltc_data.head())

# Debug function if you ever need to print the whole database
#ltc_data.to_csv("DEBUG_History.csv", index = False)

