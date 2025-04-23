#!/env/bin/usr python

def matrix_divide(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a matrix")

    if not isinstance(div, (int, float)):
        raise TypeError("Div must be a number")

    if div == 0:
        raise ZeroDivisionError("Division by 0")

#    for row in matrix:
#        if len(row) != row_length:
#            raise TypeError("Row must be of same size")
    
#   row_length = len(matrix[0])
#    for row in matrix:
#        if len(row) != row_length:
#            raise TypeError("Each row muat be same lenght")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix

