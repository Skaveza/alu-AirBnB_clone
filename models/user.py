#!/usr/bin/python3
"""
user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    users information
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
