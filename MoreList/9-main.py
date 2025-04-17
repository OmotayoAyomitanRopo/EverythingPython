#!/usr/bin/env python
multiply_by_2 = __import__('Mul_val').multiply_by_2
print_sorted_dictionary = __import__('OrderKeys').print_sorted_dictionary

a_dictionary = { 'john': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("____")
print_sorted_dictionary(new_dict)
