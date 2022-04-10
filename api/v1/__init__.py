from flask import Blueprint
from flask_restful import Resource, Api

from api.auth import auth


class V1Resource(Resource):
    @classmethod
    def get(cls):
        return {"version": "v1"}


v1 = Blueprint("v1", import_name="v1")
v1_api = Api(v1)
v1_api.add_resource(V1Resource, '/')
v1.register_blueprint(auth, url_prefix="/auth")
