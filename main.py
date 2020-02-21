from allocations import read_allocations_input
import data

# start and end dates for historic asset prices
start_date = "2019-12-31"
end_date = "2020-02-21"

# fetch portfolio's tickers and allocations
portfolio_input = read_allocations_input("portfolio")
port_tickers = portfolio_input["ticker"].tolist()

# # fetch benchmark's tickers and allocations
# bench_input = read_allocations_input("benchmark")
# bench_tickers = portfolio_input["ticker"].tolist()


print("===== Fetching Historic Prices of Assets in Portfolio =====")
port_prices = data.fetch_portfolio_prices(tickers=port_tickers, start_date=start_date, end_date=end_date)
print(port_prices)
print("===== Fetching Fundamentals of Assets in Portfolio =====")
port_fundamentals = data.fetch_portfolio_fundamentals(port_tickers)
print(port_fundamentals)

# print("===== Fetching Historic Prices of Assets in Benchmark =====")
# bench_prices = data.fetch_portfolio_prices(tickers=bench_tickers, start_date=start_date, end_date=end_date)
# print(bench_prices)
# print("===== Fetching Fundamentals of Assets in Benchmark =====")
# bench_fundamentals = data.fetch_portfolio_fundamentals(bench_tickers)
# print(bench_fundamentals)
