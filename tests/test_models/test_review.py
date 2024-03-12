#!/usr/bin/python3

"""
    test reviews
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up a Review instance for testing.
        """
        self.review = Review()

    def test_review_inherits_base_model(self):
        """
        Test if Review class inherits from BaseModel.
        """
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes(self):
        """
        Test if Review instance has required attributes.
        """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_review_to_dict(self):
        """
        Test the to_dict method of the Review instance.
        """
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["place_id"], "")
        self.assertEqual(review_dict["user_id"], "")
        self.assertEqual(review_dict["text"], "")

    def test_review_from_dict(self):
        """
        Test the from_dict method of the Review class.
        """
        review_dict = {
            "id": "123",
            "created_at": "2023-08-12T21:00:40.677911",
            "updated_at": "2023-08-12T21:00:40.677911",
            "__class__": "Review",
            "place_id": "456",
            "user_id": "789",
            "text": "Nice place, great experience!"
        }
        new_review = Review.from_dict(review_dict)
        self.assertIsInstance(new_review, Review)
        self.assertEqual(new_review.id, "123")
        self.assertEqual(new_review.created_at.isoformat(),
                         "2023-08-12T21:00:40.677911")
        self.assertEqual(new_review.updated_at.isoformat(),
                         "2023-08-12T21:00:40.677911")
        self.assertEqual(new_review.place_id, "456")
        self.assertEqual(new_review.user_id, "789")
        self.assertEqual(new_review.text, "Nice place, great experience!")


if __name__ == '__main__':
    unittest.main()
