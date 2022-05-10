#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda c: c * c), elm)) for elm in matrix]
