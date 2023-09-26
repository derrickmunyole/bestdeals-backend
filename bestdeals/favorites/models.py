import pymongo
from django.conf import settings
from django.http import JsonResponse
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError

# Create your models here.


class Favorites:
    def __init__(self):
        url = settings.MONGO_CONNECTION_URL
        client = pymongo.MongoClient(url)
        db = client['bestdeals']
        self.collection = db['favorites']

    def fetch_favorites(self, user_id):
        try:
            cursor = self.collection.find({'user_id': user_id})
            # list comprehension to serialize mongodb _id field
            results = [{**item, '_id': str(item['_id'])} for item in cursor]
            print(type(results))
            print(results)
            return results
        except PyMongoError as e:
            print(f"An error occurred while fetching favorites: {e}")
            return None

    def add_favorite(self, favorite_item):
        try:
            result = self.collection.insert_one(favorite_item)
            return {"item": str(result.inserted_id)}
        except PyMongoError as e:
            print(f"An error occurred while adding a favorite: {e}")
            return JsonResponse({"error": str(e)})

    def remove_item(self, favorite_id):
        try:
            objectId = ObjectId(favorite_id)
            query = {"_id": objectId}
            result = self.collection.delete_one(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"An error occurred while removing an item: {e}")

    def remove_items(self):
        try:
            self.collection.delete_many({})
        except PyMongoError as e:
            print(f"An error occurred while removing items: {e}")
