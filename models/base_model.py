#!/usr/bin/python3
"""base model module"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """This class is used as the base model"""
    def __init__(self, *args, **kwargs):
        """initializes all instances of the BaseModel class"""
        if kwargs:
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at with the
            current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary representation of BaseModel class"""
        inst = dict(self.__dict__)
        inst["created_at"] = self.created_at.isoformat(timespec='microseconds')
        inst["updated_at"] = self.updated_at.isoformat(timespec='microseconds')
        inst["__class__"] = self.__class__.__name__
        return inst
