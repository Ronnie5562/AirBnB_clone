#!/usr/bin/python3
"""_summary_
    This module cotains the {BaseModel} class - A class that defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """_summary_
        ==> { The BaseModel class } <==
        id: string - assign with an uuid when an instance is created
           ** the goal is to have unique id for each BaseModel **
        created_at: datetime - assign with the current datetime when an instance is created
        updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        from models import storage
        """_summary_
            This is the constructor method for initializing instances of our BaseModel
            args(tuple): it is a tuple of all positional arguments
            kwargs(dict): It is a dictionary containing all key-word arguments.
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.isoformat(value))
                    else:
                        setattr(self, key, value)
    
    def __str__(self):
        """_summary_
            Returns the string representation of BaseModel object in this format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """_summary_
            save(self): updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

