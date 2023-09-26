from django.db import models
import pymongo
from django.conf import settings

# Create your models here.
# models.py


class SearchItem:
    def __init__(self):
        url = settings.MONGO_CONNECTION_URL
        client = pymongo.MongoClient(url)
        self.db = client['bestdeals']
        self.db['flashitems'].create_index([("item_title", pymongo.TEXT)])
        self.db['items'].create_index([("item_title", pymongo.TEXT)])
        # self.collection = db['favorites']

    def search(self, query):
        flashitems = self.db['flashitems'].find(
            {"$text": {"$search": query}}).limit(5)
        items = self.db['items'].find({"$text": {"$search": query}}).limit(5)
        flash_items_results = [
            {**item, '_id': str(item['_id'])} for item in flashitems]
        items_results = [
            {**item, '_id': str(item['_id'])} for item in items]
        return list(flash_items_results) + list(items_results)
