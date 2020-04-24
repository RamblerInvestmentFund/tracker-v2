''' data.py

This module fetches the relevant data for assets in the portfolio as well as assets to be tracked
for the benchmark.

'''
import pandas as pd
import quandl
import requests
import re

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
    # data = quandl.get_table('ZACKS/CP', m_ticker=ticker, ticker=ticker)
    # data = data[['div_yield', 'beta', 'pe_ratio_f1', 'pe_ratio_12m', 'price_book', 'peg_ratio']]
    # data["comp_name"] = ticker
    # data.set_index("comp_name", inplace=True)


    url = 'https://finviz.com/quote.ashx?t=' + ticker
    html = requests.get(url).text
    return scrape_data(html)
    # return data

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
    fundamentals_df = pd.DataFrame()
    for ticker in tickers:
        ticker_fundamentals = fetch_asset_fundamentals(ticker)
        ticker_fundamentals["ticker"] = ticker
        fundamentals_df = fundamentals_df.append(ticker_fundamentals, ignore_index=True)
    fundamentals_df.set_index("ticker", inplace=True)
    return fundamentals_df

def scrape_data(html):
    """Function for scraping finviz html content.

    Args:
        html (string): html from finviz web request.

    Returns:
        : Dictionary with P/E, Forward P/E, PEG, P/B, Beta, Dividend %, and Dividend Yield

    """
    fundamentals = {}
    pattern = "(\d+\.\d{1,3})"
    fundamentals_list = ["P/E", "Forward P/E", "PEG", "P/B", "Beta", "Dividend %"]

    for fundamental in fundamentals_list:
        sequence = None
        try:
            if fundamental != "Forward P/E":
                sequence = html.split(fundamental + "</")[1].split("</b></td>")[0]
            else:
                sequence = html.split(fundamental + "</")[1].split("/span></b>")[0]
            fundamentals[fundamental] = re.findall(pattern, sequence)[0]
        except IndexError:
            fundamentals[fundamental] = None
    if fundamentals["Dividend %"] and fundamentals["Dividend %"] is not None:
        fundamentals["Dividend Yield"] = float(fundamentals["Dividend %"][0]) / 10
    else:
        fundamentals["Dividend Yield"] = None
    return fundamentals
