



class UserDbObject:

    id = None

    email = ""
    password = ""
    firstName = ""
    token = ""



    def __init__(self, json=None):
        if json is None:
            return
        self.email = json["email"]
        self.password = json["password"]
        self.firstName = json["firstName"]
        self.token = json['token']
        self.id = json["_id"]


    def toJson(self):
        return {
            "email": self.email,
            "password": self.password,
            "firstName": self.firstName,
            "token": self.token
        }
