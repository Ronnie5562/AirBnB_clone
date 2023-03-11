#!/usr/bin/python3
"""_summary_
    This module creates new instances of the Review class -- This is visible in the frontend of this project
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """_summary_
        This class inherits from a super class named - BaseModel
        place_id(str): empty string
        user_id(str): empty string
        text(str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """_summary_
            This constructor method inherits from the constructor method in BaseModel
        """
        super().__init__(*args, **kwargs)
