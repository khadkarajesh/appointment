from flask import Blueprint

from api.auth import auth
from api.auth.resources.signup_resource import SignupResource

v1 = Blueprint(import_name=__name__, name="api", url_prefix="/api/v1")
v1.register_blueprint(auth)
