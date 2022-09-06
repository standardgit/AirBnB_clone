#!/usr/bin/python3
import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.__dict__["id"])
        FileStorage.__objects[key] = obj.__dict__

    def save(self):
        with open(self.__file_path, "w") as f:
            my_dict = {key: value for key, value in self.__objects.items()}
            json.dump(my_dict, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        else:
            print("worked")
            return
