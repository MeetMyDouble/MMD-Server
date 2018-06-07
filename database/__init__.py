import pymongo
from database.UserCollection import UserCollection


class Database:

    mongoClient = None
    database = None

    userCollection = None

    def __init__(self):
        self.mongoClient = pymongo.MongoClient()
        self.database = self.mongoClient['find_my_double']
        self.userCollection = UserCollection(self.database['users'])