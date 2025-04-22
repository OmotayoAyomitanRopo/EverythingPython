#!/usr/bin/env python
Rectangle = __import__('9-Rectangle').Rectangle

My_square = Rectangle.square(100)
print("Area is {} while perimeter is {}".format(My_square.area(), My_square.perimeter()))
print(My_square)
