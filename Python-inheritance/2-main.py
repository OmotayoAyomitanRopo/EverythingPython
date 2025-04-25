#!/usr/bin/env python
is_same_class = __import__('classInstance').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of class {}".format(a, int.__name__))

if is_same_class(a, float):
    print("{} is an instance of class {}".format(a, float.__name__))

if is_same_class(a, object):
    print("{} is an instsance of classs {}".format(a, object.__name__))
