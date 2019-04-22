from flask_restful import Resource
from utils.vectorize import vectorize
from bson import ObjectId


class Health(Resource):

    def get(self):
        return {'status': 'ok'}, 200


class Recommend(Resource):

    def get(self, _id=None, n=None):
        assert _id
        assert n
        profile = {'_id': _id, 'name': 'John', 'surname': 'Smith'}
        vec = vectorize(profile)
        result = []
        for i in range(n):
            result.append(profile)
        return result, 200
