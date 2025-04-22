#!/usr/bin/env python
Rectangle = __import__('8-Rectangle').Rectangle

My_rec = Rectangle(10, 6)
My_rec2 = Rectangle(2, 43)
if My_rec is Rectangle.bigger_or_equal(My_rec, My_rec2):
    print("My rec 1 is bigger than rec 2")
else:
    print("My rec 2 is bigger than rec 1")
