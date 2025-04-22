#!/usr/bin/env python
class Rectangle:
    Number_of_instance = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.Number_of_instance += 1 #It will increment on every new instance

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2): #Static method will return the biggst rectangle base on their area

        if not isinstance(rect_1, Rectangle):
            raise TypeError("Rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("Rect_2 Must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area(): #Checks if rectangle 1 based on its area is bigger or quals to rectangle 2
            return rect_1
        else:
            return rect_2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.width for i in range(self.height)])

    def __repr__(self):
        return f"{Rectangle.width}, {Rectangle.height}"

    def __del__(self):
        Rectangle.Number_of_instance -= 1
        print("Bye bye instance ...")
