#!/usr/bin/env python
def safe_print_list_integers(my_list=[], x=0):
    try:
        nb_list = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                nb_list += 1
    except (TypeError, IndexError) as e:
        print("\nTypeerror", e)
    finally:
        print("\nCleaned up")
    return nb_list
