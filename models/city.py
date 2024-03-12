#!/usr/bin/python3

"""
get BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize City instance
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Return dictionary representation of City
        """
        city_dict = super().to_dict()
        city_dict['state_id'] = self.state_id
        city_dict['name'] = self.name
        return city_dict

    @classmethod
    def from_dict(cls, data_dict):
        """
        Create City object from dictionary
        """
        return cls(**data_dict)
