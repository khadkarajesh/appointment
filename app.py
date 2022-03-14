from flask import Flask

from api.v1 import blueprint_v1
from api.v2 import v2


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint_v1, url_prefix="/api/v1")
    app.register_blueprint(v2, url_prefix='/api/v2')
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
