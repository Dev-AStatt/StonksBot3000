from datetime import datetime
import time

from pingAPI import *


from tkinter import *
from tkinter import ttk



class GUI:

    def __init__(self, root):

        root.title("StonksBot3000")

        content = ttk.Frame(root, padding=(3,3,12,12))
        frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
        namelbl = ttk.Label(content, text="Name")
        self.name = StringVar()
        name_entry = ttk.Entry(content, textvariable=self.name)
        onevar = BooleanVar()
        twovar = BooleanVar()
        threevar = BooleanVar()

        onevar.set(True)
        twovar.set(False)
        threevar.set(True)

        one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
        two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
        three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
        ok = ttk.Button(content, text="Okay", command=self.calculate)
        cancel = ttk.Button(content, text="Cancel")

        content.grid(column=0, row=0, sticky=(N, S, E, W))
        frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
        name_entry.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
        one.grid(column=0, row=3)
        two.grid(column=1, row=3)
        three.grid(column=2, row=3)
        ok.grid(column=3, row=3)
        cancel.grid(column=4, row=3)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=3)
        content.columnconfigure(1, weight=3)
        content.columnconfigure(2, weight=3)
        content.columnconfigure(3, weight=1)
        content.columnconfigure(4, weight=1)
        content.rowconfigure(1, weight=1)


        
        
    def calculate(self, *args):
        try:
            value = float(self.name.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass



def main():
    #do not flag this as true unless you want to ping the API
    get_Historical_Data = False
    run_training_simulation = True
    display_ui = False
    if(get_Historical_Data):
        api = CoinAPI__Interface()
        api.get_historical_data_and_save_csv(
          "BITSTAMP_SPOT_BTC_USD",
          "1HRS",
          "2016-01-01T00:00:00"  
        )

        #api.get_historical_data_and_save_csv("LTC/USD", "1HRS", "2020-01-01T00:00:00", "2021-10-31T23:59:00","100")
        

    if(display_ui):
        root = Tk()
        GUI(root)
        root.mainloop()
    print("Done")


if __name__ == '__main__':
    main()


