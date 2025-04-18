#!/usr/bin/env python
raise_exception_msg = __import__('Nameexception').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
