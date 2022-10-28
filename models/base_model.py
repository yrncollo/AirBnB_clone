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
            models.storage.new(self)
