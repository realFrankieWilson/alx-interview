#!/usr/bin/env python3

"""
`Module 0-pascal_triangle`
Provides a function that returns a list of lists of integers
representing the pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's tringle of n:
      Args ->
          n: input parameter of the function

      Returns:
          List of lists of integers
          Or an empty list if n is less or equals 0
    """
    if n <= 0:
        return []

    trinagle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(trinagle[i - 1][j - 1] + trinagle[i - 1][j])
        row.append(1)
        trinagle.append(row)
    return trinagle
