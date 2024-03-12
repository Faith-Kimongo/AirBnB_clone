#!/usr/bin/python3

"""
get the BaseModel. User inherit from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from
    BaseModel class
    declare public instance of the class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        initiate the class using super class
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        return dictionary representation of User
        """
        user_dict = super().to_dict()
        user_dict['email'] = self.email
        user_dict['password'] = self.password
        user_dict['first_name'] = self.first_name
        user_dict['last_name'] = self.last_name
        return user_dict

    @classmethod
    def from_dict(cls, data_dict):
        """
        create User object from dictionary
        """
        return cls(**data_dict)
