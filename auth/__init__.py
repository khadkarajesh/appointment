from flask import Blueprint
from flask_restful import Api

from auth.resources.signup_resource import SignupResource

auth = Blueprint(name="auth", import_name=__name__)
auth_api = Api(auth)
auth_api.add_resource(SignupResource, '/signup')
