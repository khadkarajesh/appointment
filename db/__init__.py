import uuid

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = sa.create_engine("sqlite:///:memory:testdb")
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    def __init__(self):
        self.id = str(uuid.uuid4())


def init_db():
    Base.metadata.create_all(bind=engine)
