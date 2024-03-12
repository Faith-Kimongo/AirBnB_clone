#!/usr/bin/python3

"""
Defines unittests for user
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up a State instance for testing.
        """
        self.state = State()

    def test_state_inherits_base_model(self):
        """
        Test if State class inherits from BaseModel.
        """
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attributes(self):
        """
        Test if State instance has required attributes.
        """
        self.assertTrue(hasattr(self.state, "name"))

    def test_state_to_dict(self):
        """
        Test the to_dict method of the State instance.
        """
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["name"], "")

    def test_state_from_dict(self):
        """
        Test the from_dict method of the State class.
        """
        state_dict = {
            "id": "123",
            "created_at": "2023-08-12T21:00:40.677911",
            "updated_at": "2023-08-12T21:00:40.677911",
            "__class__": "State",
            "name": "California"
        }
        new_state = State.from_dict(state_dict)
        self.assertIsInstance(new_state, State)
        self.assertEqual(new_state.id, "123")
        self.assertEqual(new_state.created_at.isoformat(),
                         "2023-08-12T21:00:40.677911")
        self.assertEqual(new_state.updated_at.isoformat(),
                         "2023-08-12T21:00:40.677911")
        self.assertEqual(new_state.name, "California")


if __name__ == '__main__':
    unittest.main()
