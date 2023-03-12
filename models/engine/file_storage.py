#!/usr/bin/python3
"""_summary_
    This module contains the base class { FileStorage } that anchors the methods that performs the CRUD {Create, Read, Update, Delete} operations in every model.
    Also, it serializes instances to a JSON file and deserializes JSON file to instances:
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

models_classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City, "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """_summary_
        Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
        Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn't exist, no exception should be raised)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """_summary_
            This method returns the dictionary ==> { __objects }
        """
        return self.__objects
    
    def new(self, obj):
        """_summary_
            This method creates a new instance of a specific class.
        """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    
    def save(self):
        """_summary_
            This method serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, mode="w") as file:
            # json.dump(self.__objects, f, default=lambda obj: obj.to_dict())
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, file, indent=2)

    def reload(self):
        """_summary_
            This method deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn't exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, mode="r") as file:
                json_data = json.load(file)
            for key in json_data:
                # The code below, creates a new instance of our models_classes depending on the json_data received.
                self.__objects[key] = models_classes[json_data[key]['__class__']](**json_data[key])
        except:
            pass
        #Easier to ask for forgiveness than permission