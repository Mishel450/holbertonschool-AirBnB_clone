#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file"""
from models.base_model import BaseModel
import json


class FileStorage:
    """FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """store an object in the dictionary"""
        if obj is not None:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_data = {}
        for key, value in self.__objects.items():
            serialized_data[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_data, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        
        try:
            with open(self.__file_path, 'r') as file:
                for key, value in json.load(file).items():
                    value = BaseModel(**value)
                    self.__objects[key] = value

        except FileNotFoundError:
            pass
