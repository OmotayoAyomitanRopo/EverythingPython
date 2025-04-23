#!/usr/bin/env python
matrix_divide = __import__('div_matrix').matrix_divide

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divide(matrix, 3))
print(matrix)
