#!/usr/bin/env python
Rectangle = __import__('1_Rectangle').Rectangle

My_rec = Rectangle(2, 5)
print(My_rec.__dict__)

My_rec.width = 4
My_rec.height = 5
print(My_rec.__dict__)
