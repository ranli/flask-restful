from flask import Flask, request
from flask_restful import Api
from flask_pymongo import PyMongo
from resources.single_house_info import SingleHouseInfo
from resources.house_info_collection import HouseInfoCollection

app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)

api.add_resource(HouseInfoCollection, '/houses', resource_class_kwargs={ 'mongo': mongo })
api.add_resource(SingleHouseInfo, '/house/<string:id>', '/house',
    endpoint='single_house', resource_class_kwargs={ 'mongo': mongo })

if __name__ == '__main__':
    app.run(debug=True)
