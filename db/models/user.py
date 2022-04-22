import sqlalchemy as sa

from db import db


class User(db.Model):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    verified = sa.Column(sa.Boolean, default=False)
