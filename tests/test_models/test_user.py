#!/usr/bin/python3

"""
test for user
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up a User instance for testing.
        """
        self.user = User()

    def test_user_inherits_base_model(self):
        """
        Test if User class inherits from BaseModel.
        """
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        """
        Test if User instance has required attributes.
        """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_user_to_dict(self):
        """
        Test the to_dict method of the User instance.
        """
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], "")
        self.assertEqual(user_dict["password"], "")
        self.assertEqual(user_dict["first_name"], "")
        self.assertEqual(user_dict["last_name"], "")
        self.assertEqual(user_dict["id"], self.user.id)
        self.assertEqual(user_dict["created_at"], self.user.
                         created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], self.user.
                         updated_at.isoformat())
        self.assertEqual(user_dict["__class__"], "User")


if __name__ == '__main__':
    unittest.main()
