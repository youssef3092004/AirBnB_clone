#!/usr/bin/python3
import json
import os
class FileStorage:

    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open( self.__file_path , "w" ) as write:
            json.dump(self.__objects, write)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open (self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        else:
            self.__objects = []
    