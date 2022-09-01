#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    result = []
    for element in matrix:
        result.append(list(map(lambda x: x * x, element)))
    return result
