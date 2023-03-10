#!/usr/bin/python3
"""_summary_
    This module creates new instances of the User class -- This is visible in the frontend of this project
"""
from models.base_model import BaseModel


class User(BaseModel):
    """_summary_
        This class inherits from a super class named - BaseModel
        email(str): The user's email
        password(str): The user's password
        first_name(str): The user's first_name
        last_name(str): The user's last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
