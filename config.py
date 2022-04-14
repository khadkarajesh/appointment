import os
from urllib.parse import quote


class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    DB_SERVER = '192.168.1.56'
    DB_USERNAME = os.environ.get('DB_USER_NAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_DATABASE_NAME = os.environ.get('DB_NAME')
    DB_PORT = os.environ.get('DB_PORT')

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"postgresql://{self.DB_USERNAME}:{quote(self.DB_PASSWORD)}@{self.DB_SERVER}:{self.DB_PORT}/{self.DB_DATABASE_NAME}"


class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = '192.168.19.32'


class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __str__(self):
        print(f"{self.SQLALCHEMY_DATABASE_URI}")


class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    DATABASE_URI = 'sqlite:///:memory:'
