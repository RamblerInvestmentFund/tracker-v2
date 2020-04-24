''' allocations.py
This module handles the inputs for the tickers and respective allocations for the tracker to follow
and analyze.

TODO:
	* write method for consuming ticker and allocation input from csv
		* parse that data into appropriate data structure to be used by data and other modules

'''
import pandas as pd
import os

def read_allocations_input(portfolio_type):
	"""Function for fetching assets and weights in portfolio/benchmark.

    Args:
        portfolio_type (str): the portfolio of interest ("portfolio" or "benchmark".
        
    Returns:
        : DataFrame with columns: ticker and allocation

    """
	path = os.getcwd() + "/input/" + portfolio_type + "_input.csv"
	df = pd.read_csv(path)
	return df
