import datetime
from pingAPI import *

#---------------------------------#
#                           StonkBot3000
#   Created by Aaron Statt, Trey Chambers, and Benito Tijerina
#

retreveNewDataOnRun = False

def number_to_day(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[number]



ltc_data = pandas.read_csv("LTC Day History before.csv")

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

# # Assign day of the week number (0, 1, 2, 3, 4, 5, 6)
ltc_data["Day of the Week"] = ltc_data['Start Time'].datetime.dayofweek

# # Convert number to the written day of the week
ltc_data["Day of the Week"] = ltc_data["Day of the Week"].apply(number_to_day)

# Drop columns as the Start Time is enough for my purposes
ltc_data.drop(["End Time", "Open Time", "Close Time"], axis = "columns", inplace = True)

reorder_columns = [
    'Day of the Week',
    'Start Time',
    'Price Open',
    'Price Close',
    'Price High',
    'Price Low',
    'Volume Traded',
    'Trade Count'
]
ltc_data = ltc_data.reindex(columns = reorder_columns)

# Create a CSV file with the values so not to waste the free daily API calls
ltc_data.to_csv("LTC Day History.csv", index = False)



df = pandas.read_csv("LTC Day History.csv")

start_date = df["Start Time"] >= "2020-09-01"
end_date = df["Start Time"] <= "2020-09-30"
df[start_date & end_date]["Price High"].describe()["mean"]


df[start_date & end_date]["Price High"].descr