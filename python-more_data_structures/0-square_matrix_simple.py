#!/usr/bin/python3
def square_matrix_simple(matrix):
    # Create a new matrix with the same dimensions as the input matrix
    result_matrix = [[0 for _ in row] for row in matrix]

    # Fill in the values by squaring each element of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
