#!/usr/bin/env python
lookup = __import__('lookup').lookup

class Myclass(object):
    pass

class Myclass2(object):
    attribute = 3

    def my_method(self):
        pass

print(lookup(Myclass))
print(lookup(Myclass2))
