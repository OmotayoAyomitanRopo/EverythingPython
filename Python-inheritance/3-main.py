#!/usr/bin/env python
is_kind_of_class = __import__('Kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
    
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, int.__name__))

if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

