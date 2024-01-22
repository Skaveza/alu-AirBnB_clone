"""
This is a test for the base model file
"""
import unittest
import os
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        base_model = BaseModel()
        base_model.save()
        objects = storage.all()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, objects)
        stored_model = objects[key]
        self.assertGreater(stored_model.updated_at, stored_model.created_at)

    def test_to_dict(self):
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'],
                         my_model.updated_at.isoformat())

    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
