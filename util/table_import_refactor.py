from pingAPI import *
#
#   Methods to refactor the csv file pinged from CoinAPI.IO
#

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
    data.drop(["End Time", "Open Time", "Close Time"], axis = "columns", inplace = True)

    # Convert the Start Time to a date/time data type
    data["Start Time"] = pandas.to_datetime(data["Start Time"])
    
    #add column for day of the week, filling it with the day of the week that column Start Time is
    data["Day of the Week"] = data['Start Time'].dt.dayofweek
    
    #change intager day of the week to string, just for visualization 
    data["Day of the Week"] = data["Day of the Week"].apply(number_to_day)

    return data


