#!/usr/bin/env python
uniq_add = __import__('unique').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print(result)
