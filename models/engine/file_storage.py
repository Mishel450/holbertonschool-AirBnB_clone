#!/usr/bin/python3
"""aaa"""
from models.base_model import BaseModel


class FileStorage:
    """FileStorage"""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects["{}.{}".format(__class__.__name__, BaseModel.id)] = obj
        


