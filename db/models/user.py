import sqlalchemy as sa

from db import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
