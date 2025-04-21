#!/usr/bin/env python
class Square:
    def __init__(self, size=0):
        self.size = size # Calls the setter

    @property
    def size(self):
        return self.__size #Return or get the private attribute size

    @size.setter
    def size(self, value):
        self.__size = value # Set the private attribute
        if not isinstance(value, int):
            raise TypeError("Must be an integer")
        if value < 0:
            raise ValueError("Must be >= 0")

    def area(self):
        return self.__size ** 2 # Return the area of a size

    def my_print(self):
        if self.__size <= 0:
            print("")
        else:
            for i in range(self.__size): # Loop through the size of a square
                print("#" * self.__size) #Print the square of # character
