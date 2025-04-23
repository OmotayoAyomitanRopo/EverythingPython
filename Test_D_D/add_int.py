#!/usr/bin/env python
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("A mist be an interger")
    if not isinstance(b, (int, float)):
        raise TypeError("B must be an integer")
    return a + b
