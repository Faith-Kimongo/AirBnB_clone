#!/usr/bin/python3

"""
get BaseModel. Review class inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize Review instance
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Return dictionary representation of Review
        """
        review_dict = super().to_dict()
        review_dict['place_id'] = self.place_id
        review_dict['user_id'] = self.user_id
        review_dict['text'] = self.text
        return review_dict

    @classmethod
    def from_dict(cls, data_dict):
        """
        Create Review object from dictionary
        """
        return cls(**data_dict)
