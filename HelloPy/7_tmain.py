#!/usr/bin/env python
add_tuple = __import__('add_turple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)

new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
