#!/usr/bin/env python
safe_print_list = __import__('Printlist').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_list: {:d}".format(nb_print))
