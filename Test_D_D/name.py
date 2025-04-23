#!/usr/bin/env python
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("Must be a string")
    print("my name is {} {}".format(first_name, last_name))
