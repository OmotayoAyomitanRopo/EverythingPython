#!/usr/bin/env python
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Not an integer")
        if value < 0:
            raise ValueError("Must be greater or less than 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an int")
        if value < 0:
            raise ValueError("Must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(["#" * self.width for i in range(self.height)])

    def __repr__(self):
        return f"{Rectangle.width}, {Rectangle.height}"

    def __del__(self):
        print("Bye bye instance ...")
