#!/usr/bin/env python
def Print_square(size):
    if not isinstance(size, (int, float)):
        raise TypeError("Size must b an integer")
    if size < 0:
        raise ValueError("Size must be >= 0")

    for i in range(size):
        print("#" * size)
