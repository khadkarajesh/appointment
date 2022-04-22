import pytest

from app import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app("config.TestingConfig")
    return app


@pytest.fixture(autouse=True)
def db(app):
    from db import db
    db.app = app
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()
