#!/usr/local/bin/python3

# imports
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from matplotlib.dates import date2num

# matplotlib.finance deprecated, mpl_finance remake has to be used
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# global constants
ALPHAVANTAGE_API_KEY = "TRAYG9G8E2ZQ0LU5"

def main():

	# return data
	ts = TimeSeries(key=ALPHAVANTAGE_API_KEY, output_format="pandas")
	retrieved_data, retrieved_meta_data = ts.get_intraday(symbol="AMZN", interval="1min", outputsize="full")


	#retrieved_data['just_date'] = retrieved_data['dates'].dt.date

	# create candlesticks
	ohlc = []
	open, high, low, close, volume = retrieved_data["1. open"].values, retrieved_data["2. high"].values, retrieved_data["3. low"].values, retrieved_data["4. close"].values, retrieved_data["5. volume"].values
	date = pd.to_datetime(retrieved_data.index.values, infer_datetime_format=True)

	print(date[0])
	for i in range(0, len(date)):

		candlestick_data = date2num(date[i]), open[i], high[i], low[i], close[i], volume[i]
		print(candlestick_data)
		ohlc.append(candlestick_data)

	# plot candlesticks
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))

	candlestick_ohlc(ax1, ohlc, width=0.0003, colorup='#77d879', colordown='#db3f3f')

	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)

	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
	ax1.grid(True)

	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title("AMZN")
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
	plt.show()

if __name__ == "__main__":
	main()
