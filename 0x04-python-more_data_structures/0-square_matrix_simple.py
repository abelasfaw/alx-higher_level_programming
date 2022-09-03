#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in range(0, len(matrix)):
        result.append(list(map(lambda x: x * x, matrix[i])))
    return result
