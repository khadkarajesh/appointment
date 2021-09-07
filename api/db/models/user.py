import sqlalchemy

from api.db import BaseModel, session
import sqlalchemy as sa


class User(BaseModel):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
