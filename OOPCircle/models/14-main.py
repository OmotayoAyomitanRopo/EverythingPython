#!/usr/bin/env python
from base import Base
from rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dict = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dict)
    print(type(json_dict))
