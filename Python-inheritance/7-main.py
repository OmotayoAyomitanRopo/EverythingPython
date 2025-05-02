#!/usr/bin/env python
BaseGeometry = __import__('7-basegeo').BaseGeometry

Bg = BaseGeometry()

Bg.integer_validator("name", 9)
Bg.integer_validator("width", 34)

try:
    Bg.integer_validator("name", "john")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    Bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    Bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

