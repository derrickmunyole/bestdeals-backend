import pymongo
from django.conf import settings
from django.http import JsonResponse
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError

# Create your models here.


class Review:
    def __init__(self):
        url = settings.MONGO_CONNECTION_URL
        client = pymongo.MongoClient(url)
        db = client['bestdeals']
        self.collection = db['reviews']

    def fetch_user_reviews(self, user_id):
        try:
            cursor = self.collection.find({'user_id': user_id})
            # list comprehension to serialize mongodb _id field
            results = [{**item, '_id': str(item['_id'])} for item in cursor]
            print(type(results))
            print(results)
            return results
        except PyMongoError as e:
            print(f"An error occurred while fetching reviews: {e}")
            return None

    # All reviews for a product
    def fetch_reviews(self, item_id):
        try:
            cursor = self.collection.find({'item_id': item_id})
            # list comprehension to serialize mongodb _id field
            results = [{**item, '_id': str(item['_id'])} for item in cursor]
            print(type(results))
            print(results)
            return results
        except PyMongoError as e:
            print(f"An error occurred while fetching reviews: {e}")
            return None

    def add_review(self, review):
        try:
            result = self.collection.insert_one(review)
            return {"item": str(result.inserted_id)}
        except PyMongoError as e:
            print(f"An error occurred while adding a review: {e}")
            return JsonResponse({"error": str(e)})

    def update_review(self, review_id, updated_review):
        try:
            objectId = ObjectId(review_id)
            query = {"_id": objectId}
            new_values = {"$set": updated_review}
            self.collection.update_one(query, new_values)
        except PyMongoError as e:
            print(f"An error occurred while updating review: {e}")
            return JsonResponse({"error": str(e)})

    def remove_review(self, review_id):
        try:
            objectId = ObjectId(review_id)
            query = {"id": objectId}
            self.collection.delete_one(query)
        except PyMongoError as e:
            print(f"An error occurred while deleting review: {e}")

    def remove_reviews(self):
        try:
            self.collection.delete_many()
        except PyMongoError as e:
            print(f"An error occurred while removing reviews: {e}")
