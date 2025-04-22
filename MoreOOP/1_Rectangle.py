#!/usr/bin/env python
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self): #Will retirve the set value
        return self.__width

    @width.setter
    def width(self, value): # Set the value for width
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value): # Set value for height
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
