#!/usr/local/bin/python3

# imports
import requests, bs4, time
import retrieve_listed_entity_names as rlen

def main():

	# for checking file runtime
	start_time = time.time()

	entity_names, entity_URL_list = rlen.main()
	nordnet_base_URL = "https://www.nordnet.no"

	entity_list = [
		"Norsk Hydro",
		"Nordic Nanovector",
		"DNO",
		"PGS",
		"NEL",
		"IDEX Biometrics",
		"Panoro Energy",
		"SAS AB",
		"Thin Film Electronics",
		"Aker Solutions",
		"Targovax",
		"Elkem"
	]

	entity_index_list = []

	for entity in entity_list:

		index = entity_names.index(entity)
		entity_index_list.append(index)

	print(entity_index_list)

	for i in range(0, len(entity_index_list)):

		entity_URL = nordnet_base_URL + entity_URL_list[entity_index_list[i]]

		request = requests.get(entity_URL)
		soup = bs4.BeautifulSoup(request.text, "html.parser")

		current_price_span_class = "Typography__StyledTypography-sc-10mju41-0 iypTIw StatsBox__StyledPriceText-sc-1p4v3dm-2 gwiUDd"
		current_price = soup.find("span", {"class":current_price_span_class})

		print(entity_names[entity_index_list[i]])
		print(current_price.text)
		print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
	main()
