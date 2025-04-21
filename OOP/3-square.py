#!/usr/bin/env python
class Square:
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("Must be an int")
        if size < 0:
            raise ValueError("Size must be >= 0")

    def area(self):
        return self.__size ** 2
