from flask import jsonify

class ResponseObject:


    content = dict()

    def __init__(self, code):
        self.content['code'] = code

    def add_arg(self, key, value):
        self.content[key] = value
        return self

    def toJson(self):
        return jsonify(self.content)
