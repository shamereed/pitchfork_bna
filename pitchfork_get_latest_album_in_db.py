from pymongo import MongoClient

CONNECTION_STRING = "mongodb://localhost:27017/"
QUERY = ""

def get_database():
   client = MongoClient(CONNECTION_STRING)
   return client['best_new_albums']

def getLatestAlbumDocument():
	dbname = get_database()
	collection_name = dbname["albums"]

	for x in collection_name.find().limit(1): 
  		print(x)
  		return x