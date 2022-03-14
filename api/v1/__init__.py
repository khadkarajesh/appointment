from flask import Blueprint
from flask_restful import Resource, Api

from api.auth import auth


class V1Resource(Resource):
    @classmethod
    def get(cls):
        return {"version": "v1"}


blueprint_v1 = Blueprint("v1", import_name="v1")
v1_api = Api(blueprint_v1)
v1_api.add_resource(V1Resource, '/')
blueprint_v1.register_blueprint(auth, url_prefix="/auth")
