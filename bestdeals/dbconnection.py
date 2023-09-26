import pymongo

url = "mongodb+srv://bestdealadmin:bestdeal123@bestdeals.tgrgo4w.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)

db = client['bestdeals']
