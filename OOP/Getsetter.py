#!/usr/bin/env python
class Square:

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an int")
        if value < 0:
            raise ValueError("Size must be greater than or equals to zero")
        self.__size = value

    def area(self):
        return self.__size ** 2
