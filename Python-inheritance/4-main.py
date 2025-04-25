#!/usr/bin/env python
inherits_from = __import__('inheritfrom').inherits_from

a = True

if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))

if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
