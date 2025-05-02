#!/usr/bin/env python
class BaseGeometry:
    def area(self):
        raise Exception("area () is not implemented")

    def integer_validator(self, name, value):
        self.__name = name
        self.__value = value

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an int")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
