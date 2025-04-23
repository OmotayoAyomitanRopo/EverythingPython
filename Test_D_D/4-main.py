#!/usr/bin/env python
Print_square = __import__('print_square').Print_square

Print_square(10)

print("")
Print_square(3)

try:
    Print_square(-1)

except Exception as e:
    print(e)

try:
    Print_square("e")
except Exception as e:
    print(e)


