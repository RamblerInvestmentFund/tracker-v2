''' data.py
This module fetches the relevant data for assets in the portfolio as well as assets to be tracked
for the benchmark.

TODO:
    * write method for fetching asset data
        * daily prices for given timeframe
        * returns
        * P/E
            * Trailing
            * Forward
        * PEG
        * P/B
        * Beta
        * Dividend yield
    * write wrapper method for fetching specific asset data
        * portfolio assets
        * benchmark assets
'''
from allocations import read_allocations_input
import pandas as pd
import quandl

# df = read_allocations_input()
# print(df.head())

quandl.ApiConfig.api_key = 'mRJDZwn3giwAm1kowtFr'

''' Fields available for use from EOD Quandl request
 0   Open        1 non-null      float64
 1   High        1 non-null      float64
 2   Low         1 non-null      float64
 3   Close       1 non-null      float64
 4   Volume      1 non-null      float64
 5   Dividend    1 non-null      float64
 6   Split       1 non-null      float64
 7   Adj_Open    1 non-null      float64
 8   Adj_High    1 non-null      float64
 9   Adj_Low     1 non-null      float64
 10  Adj_Close   1 non-null      float64
 11  Adj_Volume  1 non-null      float64
 '''

def fetch_asset_prices(ticker, start_date, end_date):
    """Function for fetching individual asset's relevant data for anaysis.

    Args:
        ticker (str): The asset's ticker symbol.
        start_date (str): The start date for historic data.
        end_date (str): The end date for historic data.

    Returns:
        : object with asset's adjusted close price history for a given timeframe

    """
    asset_data = quandl.get('EOD/' + ticker, start_date=start_date, end_date=end_date)
    return asset_data["Adj_Close"]

def fetch_portfolio_prices(tickers, start_date, end_date):
    """Function for fetching historical closing prices of all tickers in portfolio.

    Args:
        tickers (list): List of tickets in the portfolio.
        start_date (str): The start date for historic closing prices.
        end_date (str): The end date for historic closing prices.

    Returns:
        : object with asset's adjusted close price history for a given timeframe

    """
    prices_df = pd.DataFrame()
    for ticker in tickers:
        # need to see what the data structure looks like back from Quandl before continuing
        prices_df[ticker] = fetch_asset_prices(ticker, start_date, end_date)
    return prices_df

prices_df = fetch_portfolio_prices(['PENN', 'AAPL'], start_date='2020-02-03', end_date='2020-02-14')
print(df)
