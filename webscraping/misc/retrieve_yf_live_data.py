#!/usr/local/bin/python3

# imports

import yfinance as yahoo_finance
import numpy as np
import pandas as pd

def main():

	selected_tickers = "NEL.OL"

	request_return_df = yahoo_finance.download(
								tickers = selected_tickers,
								period = "week",
								interval = "1m",
								group_by = "ticker",
								)

	minute_close_quotes = request_return_df["Close"].values

	for i in range(0, len(minute_close_quotes)):

		print(minute_close_quotes[i])

	print(len(minute_close_quotes))

	print(request_return_df.tail())

if __name__ == "__main__":
	main()
