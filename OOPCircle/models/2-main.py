#!/usr/bin/env python

from rectangle import Rectangle

if __name__ == '__main__':

    r2 = Rectangle(2, 4, 5, 5, 7)
    print(r2.id)

    try:
        r1 = Rectangle(3, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(3, 5)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(3, 6)
        r.x ={}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(43, 53, 6, -1, 5)
    except Exception as e:
        print(Rectangle)
        print("[{}] {}".format(e.__class__.__name__, e))


