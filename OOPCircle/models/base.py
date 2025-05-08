#!/usr/bin/env python
import json
""" Claas module
"""
class Base:
    __nb_objects = 0 # Private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id # If id value is provided assign public instance attribute with thw value
        else:
            Base.__nb_objects += 1 # If id value is not provided increment with private class attribute
            self.id = Base.__nb_objects # Then assign the new value to the public instance attribute id
            
    # Retruns the json string representation of a dict
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries :
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"

        if list_objs is not None:
            obj_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(obj_dicts)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_string)
