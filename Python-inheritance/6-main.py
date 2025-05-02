#!/usr/bin/env python
BaseGeometry = __import__('6-basegeo').BaseGeometry

Bg = BaseGeometry()

try:
    print(Bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
