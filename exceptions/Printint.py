#!/usr/bin/env python
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value, end=""))
            return True
        else:
            return False
    except Exception as e:
        print("TypeError", e)
