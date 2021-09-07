from flask import Flask

from api import v1


def create_app(config):
    app = Flask(__name__)
    app.register_blueprint(v1)
    return app
