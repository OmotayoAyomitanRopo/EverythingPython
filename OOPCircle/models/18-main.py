#!/usr/bin/env python
""" main.py test function"""
from rectangle import Rectangle
from square import Square

if __name__ == "__name__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangle_input = [r1, r2]

    Rectangle.save_to_file(list_rectangle_input)

    list_rectangle_output = Rectangle.load_from_file()

    for rect in list_rectangle_input:
        print("[{}] {}".format(id(rect), rect))

    print("____-===___")

    for rect in list_rectangle_output:
        print("[{}] {}".format(id(rect), rect))

    print("___")
    print("___")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_square_input = [s1, s2]

    Square.save_to_file(list_square_input)

    list_square_output = Square.load_from_file()

    for square in list_square_input:
        print("[{}] {}".format(id(square), square))

    print("--------")

    for square in list_sqaures_output:
        print("[{}] {}".format(id(squre), sqaure))
