#!/usr/local/bin/python3

# imports
import requests, bs4, time
from datetime import datetime as dt

import os, sys
absolute_path  = "/Users/o/Sites/github-repositories/OSL-exchange-live-watchlist/local-modules/"
sys.path.append(os.path.abspath(absolute_path))

import retrieve_sql_data as rsd

def main():

	entity_names, complete_URL = rsd.main()

	for entity in complete_URL:

		request = requests.get(entity)
		soup = bs4.BeautifulSoup(request.text, "html.parser")

		buy_price_class = "Typography__Span-sc-10mju41-0 htqjlq Typography__StyledTypography-sc-10mju41-1 famDvB StatsBox__StyledPriceText-sc-1p4v3dm-2 emJMXq"

		buy_price = soup.find_all("span", {"class" : buy_price_class})

		for i in buy_price:
			print(i.text)
		print(buy_price)
		print("\n")


		#live_time_element = soup.find_all("time")[0].text
		#live_time = dt.strptime(str(live_time_element), "%H:%M:%S")

	#print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
	main()
