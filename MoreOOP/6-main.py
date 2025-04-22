#!/usr/bin/env python
Rectangle = __import__('6-Rectangle').Rectangle

My_rec = Rectangle(3, 5)
My_rec1 = Rectangle(4, 5)
My_rec2 = Rectangle(6, 8)
print("{:d} Number of instance".format(Rectangle.Number_of_instance))
del My_rec1
print("{:d} number of instance".format(Rectangle.Number_of_instance))
del My_rec2
print("{:d} number of Instance".format(Rectangle.Number_of_instance))
