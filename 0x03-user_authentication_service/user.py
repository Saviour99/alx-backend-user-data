#!/usr/bin/env python3
"""
User Authentication
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
        Create table for Users
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(300), nullable=False)
    hashed_password = Column(String(300), nullable=False)
    session_id = Column(String(300))
    reset_token = Column(String(300))

