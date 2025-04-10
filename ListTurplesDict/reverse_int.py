#!/usr/bin/env python
def print_reversed_list_integer(my_list=[]):
    reverse_list = my_list[::-1]
    for item in reverse_list:
        print('{}'.format(item))
