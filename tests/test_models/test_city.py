#!/usr/bin/python3

"""
Defines unittests for models/city.py.
Unittest classes:
TestCity_instantiation
TestCity_save
TestCity_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up a City instance for testing.
        """
        self.city = City()

    def test_city_inherits_base_model(self):
        """
        Test if City class inherits from BaseModel.
        """
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes(self):
        """
        Test if City instance has required attributes.
        """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_city_to_dict(self):
        """
        Test the to_dict method of the City instance.
        """
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["state_id"], "")
        self.assertEqual(city_dict["name"], "")
        self.assertEqual(city_dict["id"], self.city.id)
        self.assertEqual(city_dict["created_at"],
                         self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"],
                         self.city.updated_at.isoformat())
        self.assertEqual(city_dict["__class__"], "City")

    def test_city_from_dict(self):
        """
        Test the from_dict method of the City class.
        """
        city_dict = {
            "id": "123",
            "created_at": "2023-08-15T12:00:00.369637",
            "updated_at": "2023-08-15T13:00:00.147147",
            "__class__": "City",
            "state_id": "456",
            "name": "San Francisco"
        }
        new_city = City.from_dict(city_dict)
        self.assertIsInstance(new_city, City)
        self.assertEqual(new_city.id, "123")
        self.assertEqual(new_city.created_at.isoformat(),
                         "2023-08-15T12:00:00.369637")
        self.assertEqual(new_city.updated_at.isoformat(),
                         "2023-08-15T13:00:00.147147")
        self.assertEqual(new_city.state_id, "456")
        self.assertEqual(new_city.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
