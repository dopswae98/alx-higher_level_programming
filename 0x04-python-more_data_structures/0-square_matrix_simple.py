#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squared_matrix.append(matrix[i][j]**2)
    return squared_matrix
        
