#!/usr/bin/python3
"""matrix operation module"""


def matrix_divided(matrix, div):
    """divides each element of matrix by div and returns \
            new matrix of results"""

    if(not(isinstance(matrix, list))):
        raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")
    for element in matrix:
        if(not(isinstance(element, list))):
            raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
        for data in element:
            if(not(isinstance(data, int)) and not(isinstance(data, float))):
                raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
    row_size = len(matrix[0])
    for i in range(1, len(matrix)):
        if(len(matrix[1]) != row_size):
            raise TypeError("Each row of the matrix must have the same size")
    if(not(isinstance(div, float)) and not(isinstance(div, int))):
        raise TypeError("div must be a number")
    if(div == 0):
        raise ZeroDivisionError("division by zero")
    result = []
    for lis in matrix:
        single_row = []
        for list_element in lis:
            single_row.append(round(list_element / div, 2))
        result.append(single_row)
    return result
