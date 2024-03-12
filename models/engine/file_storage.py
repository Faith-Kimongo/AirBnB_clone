#!/usr/bin/python3

"""
get json model
get path module to check for files existence
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import path


class FileStorage:
    """
    file storage class
    adds persistence storage feature to the project
    saves data using JSON format
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ gets the __objects and
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with
            key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the
        JSON file (path: __file_path)
        """
        my_dict = {}
        """Loop and convert object to dict"""
        for key, obj in self.__objects.items():
            my_dict[key] = obj.to_dict()
        """ open file in file path __file_path and save the dict """
        with open(self.__file_path, mode='w', encoding='UTF-8') as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
        """
        Deserializes the JSON file to
        __objects only if the JSON file (__file_path) exists
        Otherwise, do nothing.
        """
        if path.exists(self.__file_path):
            """ open the file and read the data """
            with open(self.__file_path, mode='r', encoding='UTF-8') as my_file:
                my_dict = json.load(my_file)
                from models.base_model import BaseModel
                for key, value in my_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
