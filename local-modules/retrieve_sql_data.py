#!/usr/local/bin/python3

# imports
import sqlite3

def main():

	def retrieve_entity_names(db_name):

		# retrieve entity_names, complete_URL from sqlite3 db
		connection = sqlite3.connect(db_name)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM entity_info;")

		entity_info = cursor.fetchall()
		entity_names, complete_URL = zip(*entity_info)

		return entity_names, complete_URL

	db_name = "OSL_exchange_live_watchlist.db"
	entity_names, complete_URL = retrieve_entity_names(db_name)

	return entity_names, complete_URL

if __name__ == "__main__":
	main()
