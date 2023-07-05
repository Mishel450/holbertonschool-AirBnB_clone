#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """store an object in the dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
