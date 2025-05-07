#!/usr/bin/env python

from base import Base

# A new class that inherits from Base
class Rectangle(Base):
    # Constructor method
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id) # A super call from th parent class, id is passed to handle autoincrement if id is none
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        # Validation for width setter
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    # Geeter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        # Validation for Height setter
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        if value <= 0:
            raise ValueError("heigth must be greater than 0")
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        # Validation for x setter
        if not isinstance(value, int):
            raise TypeError("x must be an int")
        if value < 0:
            raise ValueError("x must be greater than 0")
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        # Validation for y setter
        if not isinstance(value, int):
            raise TypeError("y must be an int")
        if value < 0:
            raise ValueError("y must be greater than 0")
        self.__y = value


    # Adding an area method to return thearea of the rectangle
    def area(self):
        return self.__width * self.__height

    # A display method that print rectangle instance
    def display(self):

        print("\n" * self.y, end="")

        for i in range(self.height):
            print(" " * self.x + "#" * self.width)
    
    # Overides string method
    def __str__(self):
        return f"[Rectangle] ({self.id}) ({self.x})/({self.y}) - ({self.width})/({self.height})"

    # assign each postional arguments to corresponding attribute
    def update(self, *args, **kwargs):
        attributes = ["id", "width", "height", "x", "y"]

        for i, value in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], value)
        # Handles keyword argument Kwargs
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value) # sets attribute with given value
                
