#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file"""
from models.base_model import BaseModel
import json
from models.user import User


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
        _dict = {"BaseModel": BaseModel,
                 "User": User}
        try:
            with open(self.__file_path, 'r') as file:
                for key, value in json.load(file).items():
                    cls = value["__class__"]
                    clas = _dict[cls]
                    obj = clas(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
