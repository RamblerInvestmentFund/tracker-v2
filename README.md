<p align="center">
  <img height=300 src="https://raw.githubusercontent.com/RamblerInvestmentFund/assets/master/rif_logo.jpeg">
</p>

# tracker-v2
2020

## Setup 
With Python 3 and pip installed run the following commands in a Terminal window to install the required packages. Make sure to be at the root of the tracker-v2 project directory.

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage
To fetch the historic prices and fundamentals of the desired portfolio, edit the portfolio_input.csv file with the appropriate ticker names and allocations. Edit the start and end dates for the historic prices in the ```data.py``` file. Then, run the following command. Output is currently printed to the terminal window.
```sh
python main.py
```
