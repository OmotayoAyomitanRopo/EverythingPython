#!/usr/bin/env python
Rectangle = __import__('5-Rectangle').Rectangle

My_rec = Rectangle(3, 6)
print("Area is {}, perimeter is {}".format(My_rec.area(), My_rec.perimeter()))

del My_rec

try:
    print(My_rec)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
