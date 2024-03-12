#!/usr/bin/python3

"""
get datetime module from datetime
get the unittest module
get os use os.path module to use to check if file exist
in teardown method to remove it
get the BaseModel module
"""

from datetime import datetime
from models.base_model import BaseModel
import os
import unittest
import json


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class
    """

    @classmethod
    def setUpClass(cls):
        """ set up function"""
        cls.my_model = BaseModel()
        cls.my_model_2 = BaseModel()
        cls.my_model.name = "My First Model"
        cls.my_model.my_number = 89

    def test_id(self):
        """ test if id is assigned """
        self.assertTrue(TestBaseModel.my_model.id)

    def test_id_type(self):
        """test id is a string"""
        self.assertTrue(type(TestBaseModel.my_model.id) == str)

    def test_id_uniq(self):
        """ test id is uniq"""
        self.assertTrue(TestBaseModel.my_model.id !=
                        TestBaseModel.my_model_2.id)

    def test_created_at(self):
        """ test created at is assigned """
        self.assertTrue(TestBaseModel.my_model.created_at)

    def test_created_at_is_datetime(self):
        """
        test created date is datetime instance
        """
        self.assertIsInstance(TestBaseModel.my_model.created_at, datetime)

    def test_updated_at(self):
        """ test updated_at at is assigned """
        self.assertTrue(TestBaseModel.my_model.updated_at)

    def test_updated_at_is_datetime(self):
        """
        test updated date is datetime instance
        """
        self.assertIsInstance(TestBaseModel.my_model.updated_at, datetime)

    def test_str(self):
        """test __str__ of an object"""
        exOutPut = "[{}] ({}) {}".format(TestBaseModel.my_model.__class__
                                         .__name__,
                                         TestBaseModel.my_model.id,
                                         TestBaseModel.my_model.__dict__)
        output = str(TestBaseModel.my_model)
        self.assertEqual(output, exOutPut)

    def test_save(self):
        """
        test save method check if the updated_at value changes
        """
        firstUpdatedValue = TestBaseModel.my_model.updated_at
        TestBaseModel.my_model.save()
        secondUpdatedValue = TestBaseModel.my_model.updated_at
        self.assertTrue(type(TestBaseModel.my_model.id) == str)
        self.assertTrue(firstUpdatedValue != secondUpdatedValue)
        """
        Test if the save method updates the JSON file.
        """
        with open('file.json', 'r') as file:
            obj_dict = json.load(file)
        prev_updated_at = self.my_model.updated_at.isoformat()
        self.my_model.save()
        with open('file.json', 'r') as file:
            updated_obj_dict = json.load(file)
        self.assertNotEqual(prev_updated_at,
                            updated_obj_dict['BaseModel.' +
                                             self.my_model.id]['updated_at'])

        """
        Test if the save method updates the updated_at attribute.
        """
        prev_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(prev_updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
        """
        test to_dict method
        confirm __class__ is added to the dict
        confirm created_at and updated_at are in isoformat
        """
        obj_dict = TestBaseModel.my_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], TestBaseModel.my_model.id)
        self.assertEqual(obj_dict['created_at'],
                         TestBaseModel.my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         TestBaseModel.my_model.updated_at.isoformat())

    def test_create_BaseModel_Dict(self):
        """
        Test creating BaseModel from dictionary
        """
        my_dict = TestBaseModel.my_model.to_dict()
        my_model = BaseModel(my_dict)
        self.assertTrue(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertTrue(my_model.id !=
                        TestBaseModel.my_model_2.id)

    def tearDown(self):
        """
        Set up teardown method
        """
        if os.path.exists("file.json"):
            os.remove("file.json")


if __name__ == "__main__":
    """
    if test is executed it runs as main
    but if it is imported it does not execute
    """
    unittest.main()
