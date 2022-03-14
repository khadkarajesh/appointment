from flask import Blueprint
from flask_restful import Resource, Api


class V2Resource(Resource):
    @classmethod
    def get(cls):
        return {"version": "v2"}


v2 = Blueprint(import_name=__name__, name="api", url_prefix="/api/v2")
api_v2 = Api(v2)
api_v2.add_resource(V2Resource, '/')
