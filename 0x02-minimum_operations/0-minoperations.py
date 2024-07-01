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

    temp = 0
    dp = 1

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                temp += i
                dp *= i
                n = n // i
                break
    return temp
