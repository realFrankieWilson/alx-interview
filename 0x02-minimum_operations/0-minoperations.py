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
    if n <= 1:
        return n

    # Loop through possible divisors of n, starting from 2 up to the square
    # root of n(inclusive).

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # if n is divisible by i, the copy all operation is performed once
            # and the pase operation is performed "n // i " times
            return i + minOperations(n // i)

    # return a prime number, meaning the minimum of operation is n
    return n
