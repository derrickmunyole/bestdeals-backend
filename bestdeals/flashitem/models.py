import pymongo
from django.conf import settings

# Create your models here.


class FlashItem:
    def __init__(self):
        url = settings.MONGO_CONNECTION_URL
        client = pymongo.MongoClient(url)
        db = client['bestdeals']
        self.collection = db['flashitems']

    def fetch_items(self):
        cursor = self.collection.find().limit(40)
        # list comprehension to serialize mongodb _id field
        results = [{**item, '_id': str(item['_id'])} for item in cursor]
        print(type(results))
        print(results)
        return results
