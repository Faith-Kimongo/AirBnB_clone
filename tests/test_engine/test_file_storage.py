#!/usr/bin/python3

"""
get the unittest module
get the patch, mock_open models from unittest.mock
get the filestorage model
get the Basemodel model
"""
import unittest
from unittest.mock import patch, mock_open
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json


class TestFileStorage(unittest.TestCase):
    """
    class to test the FileStorage model
    all the methods
    """

    def setUp(self):
        """
        setup method to create an instance of the filestorage
        """
        self.storage = FileStorage()

    def test_all(self):
        """
        test all function to see if what it returns is an
        instance of dict class
        """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, self.storage._FileStorage__objects)

    def test_new(self):
        """
        test new method  to see if it converts the key
        to (obj.__class__.__name__).(obj.id)
        """
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    @patch('json.dump')
    def test_save(self, mock_dump):
        """
        test save method using mock module to simulate
        real writing to a file
        covert dict to json object
        """
        obj = BaseModel()
        self.storage.new(obj)
        with patch('builtins.open', mock_open()) as m:
            self.storage.save()
            m.assert_called_once_with(self.storage._FileStorage__file_path,
                                      mode='w', encoding='UTF-8')
            mock_dump.assert_called_once()

    def test_reload(self):
        # Create and save an instance
        instance = BaseModel()
        instance.save()

        # Verify that the instance is stored in __objects
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, self.storage.all())

        # Manually modify the file to remove the instance
        self.storage.__objects = {}
        self.storage.save()

        # Reload the storage and verify that the instance is reloaded
        self.storage.reload()
        self.assertIn(key, self.storage.all())

        # Test if the reload method loads objects from JSON file.
        prev_objs = self.storage.all()
        self.storage.reload()
        reloaded_objs = self.storage.all()
        self.assertEqual(len(prev_objs), len(reloaded_objs))
        for key in prev_objs:
            self.assertEqual(prev_objs[key].to_dict(),
                             reloaded_objs[key].to_dict())


if __name__ == '__main__':
    unittest.main()
