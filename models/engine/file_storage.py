#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    This class manages the serialization and deserialization of instances
    to and from JSON.
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Add a new object to the dictionary __objects.
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Return the dictionary __objects.
        """
        return FileStorage.__objects

    def save(self):
        """
        Serialize __objects to the JSON file.
        """
        all_objs = FileStorage.__objects
        obj_dict = {}

        for obj_key in all_objs.keys():
            obj_dict[obj_key] = all_objs[obj_key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, values in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
