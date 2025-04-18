#!/usr/bin/env python
raise_exception = __import__('Typeerror').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
