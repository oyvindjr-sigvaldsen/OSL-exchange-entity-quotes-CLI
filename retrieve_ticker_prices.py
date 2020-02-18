#!/usr/local/bin/python3

# imports
import requests, bs4, time
from datetime import datetime as dt
from tqdm import tqdm

import os, sys
absolute_path  = "/Users/o/Sites/github-repositories/OSL-exchange-live-watchlist/local-modules/"
sys.path.append(os.path.abspath(absolute_path))

import retrieve_sql_data as rsd

def main():

	entity_names, complete_URL = rsd.main()

	entity_quotes = []

	for i in tqdm(range(140, len(entity_names))):

		request = requests.get(complete_URL[i])
		soup = bs4.BeautifulSoup(request.text, "html.parser")

		quotes_wrapper_class = "Typography__Span-sc-10mju41-0 htqjlq Typography__StyledTypography-sc-10mju41-1 famDvB StatsBox__StyledPriceText-sc-1p4v3dm-2 emJMXq"
		quotes_wrapper = soup.find_all("span", {"class" : quotes_wrapper_class})

		buy_price, sell_price = quotes_wrapper[0].text, quotes_wrapper[1].text
		high, low = quotes_wrapper[2].text, quotes_wrapper[3].text
		volume = quotes_wrapper[4].text

		print("\n")
		print(entity_names[i])

		entity_price_info = [
								float(buy_price.replace(",", ".")),
								float(sell_price.replace(",", ".")),
								float(high.replace(",", ".")),
								float(low.replace(",", ".")),
								volume
							]

		entity_quotes.append(entity_price_info)
		print(entity_price_info)
		print("\n")

		#live_time_element = soup.find_all("time")[0].text
		#live_time = dt.strptime(str(live_time_element), "%H:%M:%S")

	#print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
	main()
