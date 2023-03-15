#!/usr/bin/python3
"""
This is 2-matrix_divided module

"""


def matrix_divided(matrix, div):
    """
    function matrix_divided which divides every element in first list with div

    Args:
        matrix (list): first parameter
        div (int, float): second parameter

    Returns:
        the matrix where each and every element being divided by div
    """

    def check_equality_of_rows(matrix1):
        dims = []
        for i in range(len(matrix1)):
            dims.append(len(matrix1[i]))
        for j in range(len(dims)):
            if dims[0] != dims[j]:
                return True

    def check_int_or_float(matrix2):
        for i in range(len(matrix2)):
            for j in range(len(matrix2[i])):
                if not isinstance(matrix2[i][j], (int, float)):
                    return True

    if check_equality_of_rows(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif check_int_or_float(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    else:
        return list(map(lambda o: list(map(lambda oo: round(oo/div, 2), o)), matrix))