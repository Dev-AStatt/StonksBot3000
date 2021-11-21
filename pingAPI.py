import json
import requests
import pandas

def pingAPI():
    api_key = "Empty API Key"
    url = "https://rest.coinapi.io/v1/ohlcv/LTC/GBP/history?period_id=1DAY&time_start=2015-01-01T00:00:00&time_end=2020-10-31T23:59:00&limit=100000"
    headers = {"X-CoinAPI-Key" : api_key}
    response = requests.get(url, headers = headers)

    if(response.status_code == 429):
        # API response
        print("Too many requests.")
    else:
        # Get the information from the API
        coin_data  = json.loads(response.text)
        
        # Assign information to a DataFrame for later use
        ltc_data = pandas.DataFrame(coin_data)
        
        # Create a CSV file with the values so not to waste the free daily API calls
        ltc_data.to_csv("LTC_Day_History_FromAPI.csv", index = False)
