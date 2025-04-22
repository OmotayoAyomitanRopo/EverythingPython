#!/usr/bin/env python
Rectangle = __import__('2-Rectangle').Rectangle

My_rectangle = Rectangle(2, 3)

print(My_rectangle.__dict__)
print(type(My_rectangle))

print('------')

print("The area of my Rect is {} and perimeter {}".format(My_rectangle.area(), My_rectangle.perimeter()))

My_rectangle = Rectangle(10, 3)

print(My_rectangle.__dict__)
print(type(My_rectangle))

print('------')

print("The area of my Rect is {} and perimeter {}".format(My_rectangle.area(), My_rectangle.perimeter()))


My_rectangle = Rectangle(10, 0.9)

print("The area of my Rect is {} and perimeter {}".format(My_rectangle.area(), My_rectangle.perimeter()))

