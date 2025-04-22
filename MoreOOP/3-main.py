#!/usr/bin/env python
Rectangle = __import__('3-Rectangle').Rectangle

My_rec = Rectangle(2, 3)

print((My_rec.__dict__))
print("Area is {} and perimeter is {}".format(My_rec.area(), My_rec.perimeter()))

My_rec.width = 5
My_rec.height = 7

print(str(My_rec))
print(repr(My_rec))
print("____")
