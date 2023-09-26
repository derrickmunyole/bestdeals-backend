import pymongo
from django.conf import settings

# Create your models here.


class Item:
    def __init__(self):
        url = settings.MONGO_CONNECTION_URL
        client = pymongo.MongoClient(url)
        db = client['bestdeals']
        self.collection = db['items']

    def find(self, query):
        return self.collection.find_one(query)

    def fetch_items(self):
        cursor = self.collection.find().limit(50)
        results = [{**item, '_id': str(item['_id'])} for item in cursor]
        return results

    def fetch_platform_items(self, platform):
        cursor = self.collection.find({'platform': platform}).limit(50)
        results = [{**item, '_id': str(item['_id'])} for item in cursor]
        return results

    def fetch_category(self, query):
        cursor = self.collection.find({"category": query})
        results = [{**item, '_id': str(item['_id'])} for item in cursor]
        return results
