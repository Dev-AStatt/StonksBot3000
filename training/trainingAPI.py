import pandas as pd
import os.path
from util.table_import_refactor import *
#Class to include a training API class that will function exactly like the real API
#from a call standpoint, however calls will return historical training data.

class training_API():
    """API that functions like it is pulling real data, however it will return historic data on file"""
    active_chart_1d_ohlc = []
    active_chart_1d_volume = []
    def __init__(self, debug_mode):
        file_exists = os.path.exists("_csv_files/History_FromAPI.csv")
        if not file_exists:
            print("File 'Historical_FromAPI.csv' does not exist.")
        #if exists
        historical_data_raw = pd.read_csv('_csv_files/History_FromAPI.csv')
        self._hidden_all_history_1h_LTC = refactorData(historical_data_raw)
        print("Load Training Data sucsess")
        #generate some history to start
        self.active_chart_1h = self._hidden_all_history_1h_LTC[0:1000].copy()
        self._row_last_delevered = len(self.active_chart_1h)
         #add a moving average
        self.active_chart_1h['100ta'] = self.active_chart_1h['Price Close'].rolling(window=100, min_periods=0).mean()

       #save to debug for inspection
        if(debug_mode):
            self.active_chart_1h.to_csv("_csv_files/active_chart.csv", index = False)

    def update_ticker_data(self,symbol_id):
        """WIll update active_chart with new row of information"""
        if(symbol_id != "LTC/USD"):
            print("Function in Training API not setup for this trade yet")
            return
        #get new row from hidden history
        df_row = self._hidden_all_history_1h_LTC[self._row_last_delevered:(self._row_last_delevered + 1)].copy()
        self._row_last_delevered = self._row_last_delevered + 1
        #append row to end of dataframe
        self.active_chart_1h = self.active_chart_1h.append(df_row)
        self.update_df_analysis()
        self.print_current_update()

    #
    #   This method of doing analysis on the new updates should be moved into its own class that handles heavy math
    #
    def update_df_analysis(self):
        #re-calculate the moving average for the additional entery
        self.active_chart_1h['100ta'] = self.active_chart_1h['Price Close'].rolling(window=100, min_periods=0).mean()
        #Now refactor to get a 1 day dataframe from the 1h frame
        #self.active_chart_1h.set_index(['Start Time'])
        self.active_chart_1h['Start Time'] = pd.to_datetime(self.active_chart_1h['Start Time'])
        #   This isnt working
        #self.active_chart_1h.to_csv("_csv_files/History_Debug.csv")
        print(self.active_chart_1h.head())
        #self.active_chart_1d_ohlc = self.active_chart_1h['Price Close'].resample('1D', on="Start Time").ohlc()
        #self.active_chart_1d_ohlc = self.active_chart_1h.resample('1D')
        print(self.active_chart_1d_ohlc)
        
    def print_current_update(self):
        print(self.active_chart_1h[self._row_last_delevered -2:self._row_last_delevered -1])
