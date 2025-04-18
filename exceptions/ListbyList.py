#!/usr/bin/env python
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError

            div = a / b

        except TypeError:
            print("Wrong type")
            div = 0
        except ZeroDivisionError:
            print("Division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            newlist.append(div)
    return newlist
