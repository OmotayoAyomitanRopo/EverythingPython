#!/usr/bin/env python

from rectangle import Rectangle


if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(23, 5)
    print(r2.id)

    r3 = Rectangle(2, 4, 6, 2)
    print(r3.id)


    r4 = Rectangle(3, 4, 5, 2, 8)
    print(r4.id)
