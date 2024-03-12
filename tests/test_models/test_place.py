#!/usr/bin/python3

"""
Defines unittests for models/place.py.
Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Set up a Place instance for testing.
        """
        self.place = Place()

    def test_place_inherits_base_model(self):
        """
        Test if Place class inherits from BaseModel.
        """
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attributes(self):
        """
        Test if Place instance has required attributes.
        """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        # ... (add other attributes)

    def test_place_to_dict(self):
        """
        Test the to_dict method of the Place instance.
        """
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["city_id"], "")
        self.assertEqual(place_dict["user_id"], "")
        self.assertEqual(place_dict["name"], "")
        # ... (add other assertions)

    def test_place_from_dict(self):
        """
        Test the from_dict method of the Place class.
        """
        place_dict = {
            "id": "123",
            "created_at": "2023-08-12T21:00:40.677911",
            "updated_at": "2023-08-12T21:00:40.677911",
            "__class__": "Place",
            "city_id": "456",
            "user_id": "789",
            "name": "Luxury Villa",
            # ... (add other attributes)
        }
        new_place = Place.from_dict(place_dict)
        self.assertIsInstance(new_place, Place)
        self.assertEqual(new_place.id, "123")
        self.assertEqual(new_place.created_at.isoformat(),
                         "2023-08-12T21:00:40.677911")
        self.assertEqual(new_place.updated_at.isoformat(),
                         "2023-08-12T21:00:40.677911")
        self.assertEqual(new_place.city_id, "456")
        self.assertEqual(new_place.user_id, "789")
        self.assertEqual(new_place.name, "Luxury Villa")
        # ... (add other assertions)


if __name__ == '__main__':
    unittest.main()
