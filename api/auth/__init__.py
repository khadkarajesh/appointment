from flask import Blueprint
from flask_restful import Api

from api.auth.resources.signup_resource import SignupResource

auth = Blueprint(name="auth", url_prefix="/auth", import_name=__name__)
api = Api(auth)
api.add_resource(SignupResource, '/signup')
