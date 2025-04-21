#!/usr/bin/env python
Square = __import__('ClassException').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

my_square2 = Square()
print(type(my_square2))
print(my_square2.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)
try:
    print(my_square.__size)
except Exception as e:
    print(e)
try:
    my_square3 = Square("3")
    print(type(my_square3))
    print(my_square3.__dict__)
except Exception as e:
    print(e)

try:
    my_square4 = Square(-89)
    print(type(my_square4))
    print(mysquare4.__dict__)
except Exception as e:
    print(e)

