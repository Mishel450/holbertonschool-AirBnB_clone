#!/usr/bin/python3
"""BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """str"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """save"""

        self.update_at = datetime.now()

    def to_dict(self):
        """to_dict"""

        td = self.__dict__.copy()
        td["__class__"] = str(type(self).__name__)
        td["update_at"] = self.update_at.isoformat()
        td["created_at"] = self.created_at.isoformat()
        return (td)
