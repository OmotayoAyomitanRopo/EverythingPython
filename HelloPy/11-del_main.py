#!/usr/bin/env python
delete_at = __import__('delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
print(my_list)
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
