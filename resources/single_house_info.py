from flask_restful import fields, marshal_with, Resource, reqparse
from bson.json_util import dumps
from bson.objectid import ObjectId

resource_fields = {
    'deleted_count':   fields.String,
    'is_ok': fields.Boolean,
}

class DeleteDao(object):
    def __init__(self, deleted_count, status):
        self.deleted_count = deleted_count
        self.status = status

class SingleHouseInfo(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo']
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title')
        self.parser.add_argument('bedroom')
        self.parser.add_argument('sittingroom')
        self.parser.add_argument('bathroom')
        self.parser.add_argument('area')
        self.parser.add_argument('address')
        self.parser.add_argument('price')
        self.parser.add_argument('unit')
        self.parser.add_argument('loc')
        self.parser.add_argument('pictures')
    def get(self, id):
        dict = {'_id' : ObjectId(id)}
        x = dumps(self.mongo.db.test.find(dict))
        return x
    def put(self, id):
        pass
    @marshal_with(resource_fields)
    def delete(self, id):
        dict = {'_id' : ObjectId(id)}
        x = self.mongo.db.test.delete_one(dict)
        return DeleteDao(x.deleted_count, x.acknowledged)
    def post(self):
        args = self.parser.parse_args()
        dict = {'title' : args['title']}
        x = self.mongo.db.test.insert_one(dict)
        return dumps(x.inserted_id)
