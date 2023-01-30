import json
from pymongo import MongoClient

def get_database():
   CONNECTION_STRING = "mongodb://localhost:27017/"
   client = MongoClient(CONNECTION_STRING)
   return client['best_new_albums']
 
if __name__ == "__main__":
	dbname = get_database()
	collection_name = dbname["albums"]

	with open('best_albums.json') as file:
		file_data = json.load(file)

	if isinstance(file_data, list):
		collection_name.insert_many(file_data)
	else:
		collection_name.insert_one(file_data)