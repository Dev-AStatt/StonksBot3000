import json
import pandas as pd
import os.path
from util.table_import_refactor import *
#Class to include a training API class that will function exactly like the real API
#from a call standpoint, however calls will return historical training data.

class training_API():
    """API that functions like it is pulling real data, however it will return historic data on file"""
    def __init__(self, debug_mode):
        file_exists = os.path.exists("_csv_files/History_FromAPI.csv")
        if not file_exists:
            print("File 'Historical_FromAPI.csv' does not exist.")
        #if exists
        historical_data_raw = pd.read_csv("_csv_files/History_FromAPI.csv")
        self._hidden_all_history_LTC = refactorData(historical_data_raw)
        print("Load Training Data sucsess")
        #generate some history to start
        self.active_chart = self._hidden_all_history_LTC[0:1000].copy()
        self._row_last_delevered = len(self.active_chart)
        #save to debug for inspection
        if(debug_mode):
            self.active_chart.to_csv("_csv_files/active_chart.csv", index = False)

    def update_ticker_data(self,symbol_id):
        """WIll update active_chart with new row of information"""
        if(symbol_id != "LTC/USD"):
            print("Function in Training API not setup for this trade yet")
            return
        #get new row from hidden history
        print("Row Last delevered" + str(self._row_last_delevered))
        df_row = self._hidden_all_history_LTC[self._row_last_delevered:(self._row_last_delevered + 1)].copy()
        self._row_last_delevered = self._row_last_delevered + 1
        print(df_row)
        #append row to end of dataframe
        self.active_chart = self.active_chart.append(df_row)
        print(self.active_chart.tail())
        #self.active_chart.to_csv("_csv_files/active_chart.csv", index = False)

