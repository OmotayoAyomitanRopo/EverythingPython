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
            
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries :
            return "[]"
        else:
            return json.dumps(list_dictionaries)
