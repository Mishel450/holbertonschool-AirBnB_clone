#!/usr/bin/python3
"""BaseModel-task and class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """the class BaseModel"""

    def __init__(self, *args, **kwargs):
        """init the self"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """is the str of the self"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """this saves the time in the update_at"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """it creates a copy of the self.__dict__ and creates a [class] key
        and updates the [update_at] and the [created_at]"""

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = str(type(self).__name__)
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict
