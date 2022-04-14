import os

from dotenv import load_dotenv
from flask import Flask
from werkzeug.utils import import_string

from db import db
from v1 import v1
from v2 import v2

load_dotenv('.env')


def create_app(config: str):
    app = Flask(__name__)
    app.config.from_object(import_string(config)())
    app.register_blueprint(v1, url_prefix="/api/v1")
    app.register_blueprint(v2, url_prefix='/api/v2')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = create_app(os.environ.get('CONFIG'))
