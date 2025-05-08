#!/usr/bin/env python
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        # Validation for size setter
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        if value < 0:
            raise ValueError("size must be greater than 0")
        self.__size = value

    def __str__(self):
        return f"[square] ({self.id}) ({self.x})/({self.y}) - ({self.size})"

