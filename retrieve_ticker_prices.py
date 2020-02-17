#!/usr/local/bin/python3

# imports
import requests, bs4, time, sqlite3
from datetime import datetime as dt

def main():

	def retrieve_entity_names(db_name):

		# retrieve entity_names, entity_URL_list from sqlite3 db
		connection = sqlite3.connect(db_name)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM entity_info;")

		entity_info = cursor.fetchall()
		entity_names, entity_URL_list = zip(*entity_info)

		return entity_names, entity_URL_list


	# Global vars and other prerequisites
	db_name = "OSL_exchange_live_watchlist.db"
	nordnet_base_URL = "https://www.nordnet.no"
	start_time = time.time()

	entity_names, entity_URL_list = retrieve_entity_names(OSL_WATCHLIST_DB)

	entity_list = ["NEL"]

	entity_index_list = []

	for entity in entity_list:
		index = entity_names.index(entity)
		entity_index_list.append(index)

	print(entity_index_list)

	for i in range(0, len(entity_index_list)):

		entity_URL = nordnet_base_URL + entity_URL_list[entity_index_list[i]]
		#print(entity_URL)

		request = requests.get(entity_URL)
		soup = bs4.BeautifulSoup(request.text, "html.parser")

		live_data_wrapper_class = "Box__StyledDiv-sc-1bfv3i9-0 sFGOs"
		live_data_wrapper = soup.find("div", {"class" : live_data_wrapper_class})


		# time management
		current_time_raw = dt.now()

		#current_time = dt.strptime(dt.strftime(current_time_raw, "%H:%M:%S"), "%H:%M:%S").time()

		live_time_element = soup.find_all("time")[0].text
		live_time = dt.strptime(str(live_time_element), "%H:%M:%S")

		#live_time = dt.strptime(str(live_time_array[0].text), "%H:%M:%S").time()

		# print ticker for current entity
		#print(entity_names[entity_index_list[i]])

	#print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
	main()
