#!/usr/bin/env python
class Rectangle:
    def __init__(self, width=0, height=0): #Methon will instatiate/initialize class
        self.__width = width
        self.__height = height

    @property
    def width(self): # Getter to retirieve value
        return self.__width

    @width.setter
    def width(self, value): # Sets value for width
        if not isinstance(value, int):
            raise TypeError("Vlaue must be an integer")
        if value < 0:
            raise ValueError("Vlaue must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an int")
        if value < 0:
            raise ValueError("Value must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)
