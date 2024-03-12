#!/usr/bin/python3
"""
    This is a module test from Amenity class and your methods.
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up an Amenity instance for testing.
        """
        self.amenity = Amenity()

    def test_amenity_inherits_base_model(self):
        """
        Test if Amenity class inherits from BaseModel.
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attributes(self):
        """
        Test if Amenity instance has required attributes.
        """
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_amenity_to_dict(self):
        """
        Test the to_dict method of the Amenity instance.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["name"], "")
        self.assertEqual(amenity_dict["id"], self.amenity.id)
        self.assertEqual(amenity_dict["created_at"], self.amenity.
                         created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"], self.amenity.
                         updated_at.isoformat())
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_amenity_from_dict(self):
        """
        Test the from_dict method of the Amenity class.
        """
        amenity_dict = {
            "id": "123",
            "created_at": "2023-08-12T21:00:40.677911",
            "updated_at": "2023-08-15T13:00:00.417744",
            "__class__": "Amenity",
            "name": "Wifi"
        }
        new_amenity = Amenity.from_dict(amenity_dict)
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.id, "123")
        self.assertEqual(new_amenity.created_at.isoformat(),
                         "2023-08-12T21:00:40.677911")
        self.assertEqual(new_amenity.updated_at.isoformat(),
                         "2023-08-15T13:00:00.417744")
        self.assertEqual(new_amenity.name, "Wifi")


if __name__ == '__main__':
    unittest.main()
