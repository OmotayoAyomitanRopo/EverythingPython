#!/usr/bin/env python
safe_print_integer = __import__('Printint').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "school"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

