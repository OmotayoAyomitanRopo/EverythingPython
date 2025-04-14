#!/usr/bin/env python
search_replace = __import__('Replace').search_replace

my_list = [1, 2, 3, 4, 5, 6, 60]
new_list = search_replace(my_list, 2, 609)

print(new_list)
print(my_list)
