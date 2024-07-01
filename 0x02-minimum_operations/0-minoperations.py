#!/usr/bin/python3
"""
`Module 0-minoperations`
Provides a method that calculates the fewest number of operations needed to
result some characters in the file.
"""


def minOperations(n):
    """
    A function that calculates the fewest number of operations needed to
    result in exactly n H characters of a given value.
    Args:
        n(int): The given number.
    Returns:
        An integer, if n is imposible to achieve, 0 is returned
    """

    # Check if n is equals to zero or if n is 1
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Find the largest power of 2 that is less than or equals n
    p = 1
    while 2 * p <= n:
        p *= 2

    # if n is a power of 2, return the number of steps needed
    if n == p:
        return n // p

    # Otherwise, recursely calculate the minimum number of operations for n-p
    return (n - p) // p + 1 + n // p
