#!/usr/bin/python3
"""Defines FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class FileStorage
    Represents an abstracted storage test_engine.
    It serializes instances to a JSON file and deserializes
    JSON file to instances.

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """ create a new object."""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file."""
        object_dict = {}
        for obj in self.__objects:
            object_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        try:
            with open(self.__file_path) as file:
                data = json.load(file)
                for item in data.values():
                    class_name = item['__class__']
                    self.new(eval(class_name + "(**" + str(item) + ")"))
        except FileNotFoundError:
            pass