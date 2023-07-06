#!/usr/bin/python3
"""BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        """init"""

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
        """str"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """save"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict"""

        td = self.__dict__.copy()
        td["__class__"] = str(type(self).__name__)
        td["updated_at"] = self.updated_at.isoformat()
        td["created_at"] = self.created_at.isoformat()
        return (td)
