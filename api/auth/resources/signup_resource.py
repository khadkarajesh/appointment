from flask import request
from flask_restful import Resource

from api.auth.managers.auth_manager import register_user
from api.auth.schemas.user_schema import UserSchema
from api.db import session


class SignupResource(Resource):
    def post(self):
        user = UserSchema().load(request.get_json(), session=session)
        return register_user(user)
