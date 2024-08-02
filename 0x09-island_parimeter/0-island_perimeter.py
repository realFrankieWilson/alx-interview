#!/usr/bin/python3
"""Module `0-island_perimeter`
Provides a function that returns described in grid
"""


def island_perimeter(grid):
    """
    A function that returns the perimeter of the island described in grid
    Args:
        grid(list): list of integers.
    Returns:
        Perimeter of a grid island
    """

    perim = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:    # If it's land, check all sides
                # Up
                if i == 0 or grid[i - 1][j] == 0:
                    perim += 1
                # Down
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perim += 1
                # Left
                if j == 0 or grid[i][j - 1] == 0:
                    perim += 1
                # Right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perim += 1
    return perim
