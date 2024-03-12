#!/usr/bin/python3

"""
get BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
    Attributes:
        name (str): The name of the amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize Amenity instance
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Return dictionary representation of Amenity
        """
        amenity_dict = super().to_dict()
        amenity_dict['name'] = self.name
        return amenity_dict

    @classmethod
    def from_dict(cls, data_dict):
        """
        create Amenity object from dictionary
        """
        return cls(**data_dict)
