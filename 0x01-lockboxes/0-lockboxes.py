#!/usr/bin/python3

"""
`Module 0-lockboxes` Provides a function that determins if all the boxes
can be open or not.
"""


def canUnlockAll(boxes):
    """
    A function that determines if all the boxes can be opend.
    Args:
        boxes (List(String)): a list of lists.
    Returns:
        True(if all boxes can be opened).
        False(if otherwise).
    """

    box_len = len(boxes)
    visited = [False] * box_len
    visited[0] = True

    queue = [0]

    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if key < box_len and not visited[key]:
                visited[key] = True
                queue.append(key)
    return all(visited)
