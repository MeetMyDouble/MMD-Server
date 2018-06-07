from misc.Crypto import encryptPassword
from database.dbObjects.UserDbObject import UserDbObject
import uuid

class UserCollection:

    userCollection = None

    def __init__(self, collection):
        self.userCollection = collection


    def user_exists(self, userdbobject):
        user = self.userCollection.find_one({"email" : userdbobject.email})
        return user is not None

    def create_user(self, userdbobject):

        userdbobject.password = encryptPassword(userdbobject.password)
        userdbobject.token = str(uuid.uuid3(uuid.NAMESPACE_URL, userdbobject.password + userdbobject.email))
        if self.user_exists(userdbobject) is not True:
            self.userCollection.insert_one(userdbobject.toJson())

    def find_user_with_email(self, email):
        jsonUser = self.userCollection.find_one({"email": email})

        if jsonUser is not None:
            return UserDbObject(jsonUser)
        return None
