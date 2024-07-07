#!/usr/bin/python3
"""
FileStorage class for managing object instances and their JSON serialization.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Review": Review,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,  # This line is a duplicate and should be removed.
}

class FileStorage:
    """
    FileStorage class for managing object instances and their JSON serialization.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store object instances.

    Methods:
        __init__(self): Initializes the FileStorage object.
        all(self): Returns all stored object instances.
        new(self, obj): Adds a new object instance to the __objects dictionary.
        save(self): Saves the __objects dictionary to the JSON file.
        reload(self): Reloads the __objects dictionary from the JSON file.
    """

    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        """
        Initializes the FileStorage object.
        """
        pass

    def all(self):
        """
        Returns all stored object instances.

        Returns:
            dict: A dictionary containing all stored object instances.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object instance to the __objects dictionary.

        Args:
            obj (object): The object instance to be added.

        Raises:
            ValueError: If the object class is not found in the classes dictionary.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Saves the __objects dictionary to the JSON file.
        """
        with open(self.__file_path, "w") as write:
            json.dump(self.__objects, write)

    def reload(self):
        """
        Reloads the __objects dictionary from the JSON file.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for key, serialized_obj in serialized_objects.items():
                    class_name = serialized_obj['__class__']
                    self.__objects[key] = classes[class_name](**serialized_obj)
        else:
            self.__objects = {}
