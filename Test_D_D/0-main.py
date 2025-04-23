#!/usr/bin/env python
add_integer = __import__('add_int').add_integer

Result = add_integer(6, 8)
print(Result)
print(add_integer(4, -5))
print(add_integer(43))
print(add_integer(100.3, -4))
try:
    print(add_integer(2, "SDS"))
except Exception as e:
    print(e)

try:
    print(add_integer(None))
except Exception as e:
    print(e)
