#!/usr/bin/python3
"""BaseModel-task and class BaseModel"""
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel:
    """the class BaseModel"""

    def __init__(self, *args, **kwargs):
        """init the self"""

        dformat = "%Y-%m-%dT%H:%M:%S.%f"
        if (kwargs):
            self.id = kwargs["id"]
            self.created_at = datetime.strptime(kwargs["created_at"], dformat)
            self.updated_at = datetime.strptime(kwargs["updated_at"], dformat)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """is the str of the self"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """this saves the time in the update_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """it creates a copy of the self.__dict__ and creates a [class] key
        and updates the [update_at] and the [created_at]"""

        td = self.__dict__.copy()
        td["__class__"] = str(type(self).__name__)
        td["updated_at"] = self.updated_at.isoformat()
        td["created_at"] = self.created_at.isoformat()
        return (td)
