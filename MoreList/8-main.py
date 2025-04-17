#!/usr/bin/env python
simple_delete = __import__('del_keys').simple_delete
print_sorted_dictionary = __import__('OrderKeys').print_sorted_dictionary

a_dictionary = { 'Language': "c", 'number': 89, 'track': "low", 'ids': [1, 2, 3] }

new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)

print("++++====")
print_sorted_dictionary(new_dict)
