#!/usr/bin/env python
element_at = __import__('Retrive').element_at

my_list = [1, 2, 3, 4, 5, 6]
idx = 2
print("element at index {:d} is {}".format(idx, element_at(my_list, idx)))
