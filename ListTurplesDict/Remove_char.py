#!/usr/bin/env python
def no_c(my_string):
    return ''.join([char for char in my_string if char not in ('c', 'C')])
