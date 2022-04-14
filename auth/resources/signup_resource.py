from flask_restful import Resource


class SignupResource(Resource):
    @classmethod
    def get(cls):
        return {'testing': 'get'}
