#!/usr/local/bin/python3

# imports
import requests, bs4
import pandas as pd

def main():

	# retrieve_num_table_pages

	page_num = 1
	NO_ticker_list_base_URL = "https://www.nordnet.no/market/stocks?exchangeCountry=NO"

	def retrieve_num_pages(page_num, NO_ticker_list_base_URL):

		request = requests.get(NO_ticker_list_base_URL)
		soup = bs4.BeautifulSoup(request.text, "html.parser")

		page_num_a_class = "c0210 c0221 c0213 sm c02441"
		num_pages = soup.find_all("a", {"class":page_num_a_class})

		# +2 -> taking into account list() index [0] and loop interation to come
		return int(len(num_pages)+2)

	NUM_PAGES = retrieve_num_pages(page_num, NO_ticker_list_base_URL)

	def retrieve_entity_info(
							NUM_PAGES,
							NO_ticker_list_URL
							):

		# def global vars
		entity_names = []
		entity_URL_list = []

		for page_num in range(1, NUM_PAGES):

			NO_ticker_list_URL = "https://www.nordnet.no/market/stocks?page=%d&exchangeCountry=NO" % page_num

			request = requests.get(NO_ticker_list_URL)
			soup = bs4.BeautifulSoup(request.text, "html.parser")

			table_row_elements = soup.find_all("td")
			table_row_elements = [table_row for table_row in table_row_elements]

			index_interval = 22
			entity_name_index = 3

			# 22 -> num td per tr tag
			num_tickers = int(len(table_row_elements)/index_interval)

			for i in range(0, num_tickers):
				
				entity = table_row_elements[entity_name_index].find("a")

				entity_names.append(entity.text)
				entity_URL_list.append(entity["href"])

				entity_name_index += index_interval

		return entity_names, entity_URL_list

	NO_ticker_list_URL = "https://www.nordnet.no/market/stocks?page=%d&exchangeCountry=NO" % page_num

	entity_names, entity_URL_list = retrieve_entity_info(
														NUM_PAGES,
														NO_ticker_list_URL,
														)

	print(entity_names)
	print(entity_URL_list)

if __name__ == "__main__":
	main()
