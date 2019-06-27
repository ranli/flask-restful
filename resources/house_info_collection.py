from flask_restful import Resource
from bson.json_util import dumps

class HouseInfoCollection(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo']
    def get(self):
        x = dumps(self.mongo.db.test.find().limit(100))
        return x
