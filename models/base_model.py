#!/usr/bin/env python3

"""
The `BaseModel` class defines a base model
with unique ID and timestamps for creation and last
update, along with methods for saving and converting to a dictionary format.
"""

from datetime import datetime
import uuid
import models as models
from __init__ import storage

class BaseModel:
    """BaseModel class defines a base model with unique ID and timestamps."""

    def __init__(self, *args, **kwargs):
        """Initialize object with unique ID and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
                    
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the 'updated_at' timestamp."""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert object to a dictionary."""
        dic = dict()
        dic["__class__"] = self.__class__.__name__
        dic["id"] = self.id
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        for key, value in self.__dict__.items():
            if key not in ("id", "created_at", "updated_at"):
                dic[key] = value
        return dic
