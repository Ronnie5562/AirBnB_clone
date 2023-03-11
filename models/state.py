#!/usr/bin/python3
"""_summary_
    This module creates new instances of the State class -- This is visible in the frontend of this project
"""
from models.base_model import BaseModel


class State(BaseModel):
    """_summary_
        This class inherits from a super class named - BaseModel
        name(str): empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """_summary_
            This constructor method inherits from the constructor method in BaseModel
        """
        super().__init__(*args, **kwargs)
