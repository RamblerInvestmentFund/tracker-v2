''' data.py

This module fetches the relevant data for assets in the portfolio as well as assets to be tracked
for the benchmark.

TODO:
    * write logic for handling non-US assets (LVMUY)

'''
import pandas as pd
import quandl

quandl.ApiConfig.api_key = 'mRJDZwn3giwAm1kowtFr'

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

def fetch_asset_fundamentals(ticker):
    """Function for fetching company profile data for a given asset.

    Args:
        ticker (str): Ticker of asset of interest.

    Returns:
        : Pandas DataFrame with dividend yield, beta, forward pe, ttm pe, p/b, and peg

    """
    data = quandl.get_table('ZACKS/CP', m_ticker=ticker, ticker=ticker)
    data = data[['div_yield', 'beta', 'pe_ratio_f1', 'pe_ratio_12m', 'price_book', 'peg_ratio']]
    data["comp_name"] = ticker
    data.set_index("comp_name", inplace=True)
    return data

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

def fetch_portfolio_fundamentals(tickers):
    """Function for fetching company profile for a list of assets.

    Args:
        tickers (list): List of tickers of interest.

    Returns:
        : Pandas DataFrame with dividend yield, beta, forward pe, ttm pe, p/b, and peg

    """
    fun_df = pd.DataFrame()
    for ticker in tickers:
        fun_df = fun_df.append(fetch_asset_fundamentals(ticker))
    return fun_df
