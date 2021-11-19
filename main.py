import datetime
from pingAPI import *

#-----------------------------------------------------------------------------------------------------------#
#                           StonkBot3000                                                                    #
#   Created by Aaron Statt, Trey Chambers, and Benito Tijerina                                              #   
#                                                                                                           #
#   we have setup an API link to CoinAPI.io that compiles multiple exchanges and can return alot of         #
#   coin data.  The API is free for hobby projects but only allows 100 queries per day.                     #
#   For training we can export the queried data to a csv file, then read it over and over while testing.    #
#                                                                                                           #
#   The following code uses a pre-existing csv file (That is in the git dir)                                #
#                                                                                                           #
#-----------------------------------------------------------------------------------------------------------#

#   References:
#   https://jamesgeorgedunn.com/2020/10/05/using-python-and-pandas-to-analyse-cryptocurrencies-with-coinapi/
#   https://pandas.pydata.org/getting_started.html


def number_to_day(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[number]


#ltc_data is a panda data structure that is kinda like an excel sheet
ltc_data = pandas.read_csv("LTC_Day_History_FromAPI.csv")

ltc_data.rename(columns = {
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

# Convert the Start Time to a date/time data type
ltc_data["Start Time"] = pandas.to_datetime(ltc_data["Start Time"])

# Drop columns of data we dont need
ltc_data.drop(["End Time", "Open Time", "Close Time"], axis = "columns", inplace = True)

print(ltc_data.tail())

# Debug function if you ever need to print the whole database
#ltc_data.to_csv("DEBUG_History.csv", index = False)
#Test