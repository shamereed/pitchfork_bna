import json
from pymongo import MongoClient

outputFile = 'best_albums.json'
CONNECTION_STRING = "mongodb://localhost:27017/"


def get_database():
    client = MongoClient(CONNECTION_STRING)
    return client['best_new_albums']


if __name__ == "__main__":
    dbname = get_database()
    collection_name = dbname["albums"]

    with open(outputFile) as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        collection_name.insert_many(file_data)
    else:
        collection_name.insert_one(file_data)
