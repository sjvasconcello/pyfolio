
# %%
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.optimize as optimization

# %%
stocks = ['MSFT','META','TSLA','DB','AMZN']

start_date = '2018-01-01'
end_date =  '2024-01-01'
interval = '1d'

def download_data():
    # name of the stock (key) - stock values (2018-2023)

    stock_data = {}

    for stock in stocks:
        ticker = yf.Ticker(stock)
        stock_data[stock] = ticker.history(interval=interval, 
                                           start=start_date, 
                                           end=end_date)['Close']

    return pd.DataFrame(stock_data)


def show_data(data):
    data.plot(figsize=(10,5))
    plt.show()

if __name__ == '__main__':
    dataset = download_data()
    show_data(dataset)


# %%
