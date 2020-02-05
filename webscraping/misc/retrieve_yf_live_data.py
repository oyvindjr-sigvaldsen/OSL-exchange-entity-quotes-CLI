#!/usr/local/bin/python3

# imports

import yfinance as yahoo_finance

def main():

	selected_tickers = "NEL.OL"

	request_return_df = yahoo_finance.download(
								tickers = selected_tickers,
								period = "week",
								interval = "1m",
								group_by = "ticker",
								)

	print(request_return_df)

if __name__ == "__main__":
	main()
