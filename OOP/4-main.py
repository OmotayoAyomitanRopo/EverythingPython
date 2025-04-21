#!/usr/bin/env python
Square = __import__('Getsetter').Square

my_square = Square(89)
print("Area {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "Hello 9"
    print("Areea {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
