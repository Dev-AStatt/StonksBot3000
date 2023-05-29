import json
import requests
import pandas
from config import *

class CoinAPI__Interface():

    SANDBOX_base_url = 'https://rest-sandbox.coinapi.io/v1/ohlcv/'
    PRODUCTION_base_url = 'https://rest.coinapi.io/v1/ohlcv/'
    headers = {'X-CoinAPI-Key' : api_key}



    def print_periods(self):
        """Get full list of supported time periods availabe for requesting OHLCV data"""
        url = 'https://rest.coinapi.io/v1/ohlcv/periods'
        response = requests.get(url, headers=self.headers)
        print(response.text)



    def print_symbols(self):
        """Get full list of supported symbols available"""
        url = 'https://rest.coinapi.io/v1/symbols'
        response = requests.get(url, headers=self.headers)
        print(response)
        print(response.text)


    def _check_response(self, response):
        if(response.status_code == 429):
            print("Too many requests.")
            return False
        elif(response.status_code == 401):
            print("Unauthorized -- Your API Key is wrong")
            return False
        elif(response.status_code == 400):
            print("Bad Request -- There is something wrong with your request")
            return False
        elif(response.status_code == 403):
            print("Forbidden -- Your API key doesn't have enough privilages to access this resource")
            return False
        elif(response.status_code == 404):
            print("I think this is a bad URL?")
            return False
        elif(response.status_code == 550):
            print("No data -- You requested specific single item that we don't have at this moment")
            return False
        
        else:
            return True

    def _get_response(self,url):
        response = requests.get(url, headers=self.headers)
        print(response)
        #Check if API responds any Errors
        if(self._check_response):
            # Get the information from the API
            coin_data  = json.loads(response.text)
            # Assign information to a DataFrame for later use
            data = pandas.DataFrame(coin_data)
            #Return data returned from api as pandas dataframe
            return data
        else:
            return False

    def get_latest_sandbox_data(self, symbol_id, period, limit):
        """Sandbox Interface with Coin API"""
        #he sandbox environment is provided for development and non-production use-cases, it has few differences in comparison to the production one:
        #   You still need active API Key to access the sandbox; it can be a free one.
        #   We do not provide any support or SLA for this environment.
        #   You cant query for the historical data more than one day back.
        #   The limit parameter default and the maximum value is set to 10.
        #   Real-time and historical data is limited to specific data sources: COINBASE, GEMINI, testnets, UAT environments and ECB (European Central Bank).
        #   Data could be invalid/fake or delayed.
        #   API changes could be visible faster on the sandbox than in the production environment.
        #GET /v1/ohlcv/{symbol_id}/latest?period_id={period_id}&limit={limit}&include_empty_items={include_empty_items}

        # putting together the url for request
        url = self.SANDBOX_base_url + symbol_id
        url = url + '/latest?period_id=' + period
        url = url + '&limit=' + limit
        url = url + '&include_empty_items={include_empty_items}'
        return self._get_response(url)

    def _get_historical_data(self, symbol_id, period, time_start, limit = "100"):
        """Private Method Get historical data """
        #GET /v1/ohlcv/{symbol_id}/history?period_id={period_id}&time_start={time_start}&time_end={time_end}&limit={limit}&include_empty_items={include_empty_items}
        url = self.PRODUCTION_base_url + symbol_id
        url = url + '/history?period_id=' + period
        url = url + '&time_start=' + time_start
        #url = url + '&time_end=' + time_end
        url = url + '&limit=' + limit
        return self._get_response(url)

    def get_historical_data_and_save_csv(self, symbol_id, period, time_start, limit="100"):
        """method will call api for historical data and save to csv for training"""
        #get historical data from historical data method
        historical_data = self._get_historical_data(symbol_id,period, time_start, limit)            # Create a CSV file with the values so not to waste the free daily API calls
        historical_data.to_csv("_csv_files/History_FromAPI.csv", index = False)


