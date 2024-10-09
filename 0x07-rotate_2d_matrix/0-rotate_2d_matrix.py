#!/usr/bin/python3
"""
Solution 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate the given n X n 2D matrix 90 degrees clockwise in place

    Args:
        matrix (list of list of int): The 2D matrix to be rotated.
    """
    n = len(matrix)

    # Revers matrix
    matrix.reverse()

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
