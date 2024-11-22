#!/usr/bin/env python3

"""
Authentication module
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Perform hashing of password
    """

    pw = password.encode("utf-8")
    hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
    return hashed_pw


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """rEGISTER NEW USERS TO THE DB
        """
        
        try:
            self._db.find_user_by(email=email)

        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f"User {email} already exists")
