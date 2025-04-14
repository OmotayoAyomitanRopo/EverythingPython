#!/usr/bin/env python
square_matrix_simple = __import__('Matrix').square_matrix_simple

matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
