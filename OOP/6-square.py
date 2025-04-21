#!/usr/bin/env python
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size # Will return, retrieve or get the size

    @size.setter
    def size(self, value):
        self.__size = value # This will assign or set value to size
        if not isinstance(value, int):
            raise TypeError("Not an integer")
        if value < 0:
            raise ValueError("Value must be greatewr than 0")

    @property
    def position(self):
        return self.__position # Will retrive the value
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("Position must be a turple of 2 pos int")
        self.__position = value

    def area(size):
        return self.__size ** 2

    def my_print(self):
        if self.__size <= 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print()

            # Print the square with horizontal offset (spaces)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


