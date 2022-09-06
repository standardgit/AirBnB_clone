#!/usr/bin/python3
""" Base Class Module """

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ Base class"""

    def __init__(self, *arg, **kwargs):
        if kwargs is not None:
            for keys, value in kwargs.items():
                if keys != '__class__':
                    if keys == 'created_at' or keys == 'updated_at':
                        self.__dict__[keys] = datetime.fromisoformat(value)
                    else:
                        self.__dict__[keys] = value
        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.my_number = 98
            self.name = "My First Model"
            storage.new(self)
            

    def __str__(self):
        """print a base model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        self.updated_at = self.updated_at.isoformat()
        self.created_at = self.created_at.isoformat()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        of the instance """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
