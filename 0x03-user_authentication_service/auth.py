#!/usr/bin/env python3

"""
Authentication module
"""

import bcrypt

def _hash_password(password: str) -> bytes:
    """Perform hashing of password
    """

    pw = password.encode("utf-8")
    hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
    return hashed_pw
