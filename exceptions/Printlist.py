#!/usr/bin/env python
def safe_print_list(my_list=[], x=0):
    try:
        nb_print = 0
        for i in range(x): # Loops through x element in my list
            print(my_list[i], end="")
            nb_print += 1
        print()
        return nb_print
    except Exception as e: # This will catch any error that occur
        print("An error occured:", e)

