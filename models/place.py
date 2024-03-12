#!/usr/bin/python3

"""
get BaseModel. Place class inherits from the BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represent a place.
    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initialize Place instance
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Return dictionary representation of Place
        """
        place_dict = super().to_dict()
        place_dict['city_id'] = self.city_id
        place_dict['user_id'] = self.user_id
        place_dict['name'] = self.name
        place_dict['description'] = self.description
        place_dict['number_rooms'] = self.number_rooms
        place_dict['number_bathrooms'] = self.number_bathrooms
        place_dict['max_guest'] = self.max_guest
        place_dict['price_by_night'] = self.price_by_night
        place_dict['latitude'] = self.latitude
        place_dict['longitude'] = self.longitude
        place_dict['amenity_ids'] = self.amenity_ids
        return place_dict

    @classmethod
    def from_dict(cls, data_dict):
        """
        Create Place object from dictionary
        """
        return cls(**data_dict)
