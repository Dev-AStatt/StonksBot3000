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

class CoinAPI_Interface():
    
    base_url = 'https://rest.coinapi.io/v1ohlcv/'
    headers = {'X-CoinAPI-Key' : 'Empty-API-Key'}

    def _get_response(self,url):
        return requests.get(url, headers=headers)

    def get_periods(self):
        """Get full list of supported time periods availabe for requesting OHLCV data"""
        url = 'https://rest.coinapi.io/v1/ohlcv/periods'
        self._get_response(url,self.headers)

     def get_latest_data(self, symbol_id, period, limit):
        """ note """
        #GET /v1/ohlcv/{symbol_id}/latest?period_id={period_id}&limit={limit}&include_empty_items={include_empty_items}

        # putting together the url for request
        url = self.base_url + symbol_id
        url = url + '/latest?period_id=' + period
        url = url + '&limit=' + limit
        url = url + '&include_empty_items={include_empty_items}'
        return _get_response(url)

    def get_historical_data(self, symbol_id, period, time_start, time_end, limit):
        """Get historical data """
        #GET /v1/ohlcv/{symbol_id}/history?period_id={period_id}&time_start={time_start}&time_end={time_end}&limit={limit}&include_empty_items={include_empty_items}
        url = self.base_url + symbol_id
        url = url + '/history?period_id=' + period_id
        url = url + '&time_start=' + time_start
        url = url + '&time_end=' + time_end
        url = url + '&limit=' + limit
        url = url + '&include_empty_items={include_empty_items}'
        return _get_response(url)

        
