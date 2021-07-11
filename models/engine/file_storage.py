#!/usr/bin/python3
"""
filestorage module
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """FileStorage class"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = dict()
        for k, obj in FileStorage.__objects.items():
            new_dict[k] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dict_json = json.load(f)

                for dictionary in dict_json.values():
                    name_class = eval(dictionary['__class__'])
                    new_instance = name_class(**dictionary)
                    self.new(new_instance)
