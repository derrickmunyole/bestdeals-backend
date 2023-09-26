
import pymongo

from django.conf import settings


class User:

    def __init__(self):
        # Use Django settings to contain your database connection credentials
        url = settings.MONGO_CONNECTION_URL
        client = pymongo.MongoClient(url)
        db = client['bestdeals']
        self.collection = db['User']

    def insert(self, data):
        return self.collection.insert_one(data)

    def update_user(self, email, updated_data):
        query = {'email': email}
        new_values = {"$set": updated_data}
        result = self.collection.update_one(query, new_values)
        if result.matched_count > 0:
            print(f"Updated {result.matched_count} user(s)")
        else:
            print("No users found to update")

    def get_user(self, query):
        return self.collection.find_one({'email': query})

    def delete(self, query):
        return self.collection.delete_one(query)
