#!/usr/local/bin/python3

# imports
import requests, bs4, sqlite3

def main():

	def retrieve_num_pages(NO_ticker_list_base_URL, backtrack_index_num_pages):

		request = requests.get(NO_ticker_list_base_URL)
		soup = bs4.BeautifulSoup(request.text, "html.parser")

		anchor_tags = soup.find_all("a")
		num_pages = anchor_tags[len(anchor_tags)-backtrack_index_num_pages].text

		return num_pages

	def retrieve_entity_info(num_pages):

		# def global vars
		entity_names = []
		entity_URL_list = []

		for page_num in range(1, int(num_pages)+1):

			print(page_num)
			NO_ticker_list_URL = "https://www.nordnet.no/market/stocks?page=" + str(page_num) + "&exchangeCountry=NO"

			request = requests.get(NO_ticker_list_URL)
			soup = bs4.BeautifulSoup(request.text, "html.parser")

			table_row_elements = soup.find_all("td")
			table_row_elements = [table_row for table_row in table_row_elements]

			# 22 = number of td tags per tr tag
			index_interval = 22
			entity_name_index = 3
			num_tickers = int(len(table_row_elements)/index_interval)

			for i in range(0, num_tickers):

				entity = table_row_elements[entity_name_index].find("a")

				entity_names.append(entity.text)
				entity_URL_list.append(entity["href"])

				entity_name_index += index_interval

		return entity_names, entity_URL_list

	# prerequisties def retrieve_num_pages()
	NO_ticker_list_base_URL = "https://www.nordnet.no/market/stocks?exchangeCountry=NO"
	backtrack_index_num_pages = 19

	num_pages = retrieve_num_pages(NO_ticker_list_base_URL, backtrack_index_num_pages)
	entity_names, entity_URL_list = retrieve_entity_info(num_pages)

	for i in entity_names:
		print(i)


	#connection = sqlite3.connect("OSL_exchange_live_watchlist.db")
	#cursor = connection.cursor()

	#for i in range(0, len(entity_names)):

	#	cursor.execute("""INSERT INTO entity_info(entity_name, entity_URL)
	#		VALUES(?, ?)""", (entity_names[i], entity_URL_list[i]))
	#	connection.commit()

	#connection.close()

if __name__ == "__main__":
	main()
