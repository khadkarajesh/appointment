from db import session


def register_user(user):
    session.add(user)
    session.commit()
