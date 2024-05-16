#!/usr/bin/env python3
import json
class FileStorage:

    __objects = dict()
    __file_path = "examle"

    def all(self):
        return self.__objects

    def new(self, obj):
        pass

    def save(self):
        with open(self.__file_path, "w") as op:
            json.dump(self.__objects, op)

    def reload(self):
        if self.__file_path:
            with open(self.__file_path, "r") as op:
                json_data = json.load(op)
                self.__objects = json_data
        else:
            return
        
