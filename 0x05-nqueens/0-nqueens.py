#!/usr/bin/python3
import sys
"""
The Nqueen solution
"""


def print_solutions(solutions):
    """Print all the solutions to the N queens problem.

    Args:
        solutions (list): A list of solutions where each solution is a list of
        queens positions.
    """
    for sol in solutions:
        print(sol)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The current state of the board.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.

    Returns:
        bool: True if it's safe to place the queen, False if otherwise.
    """
    for i in range(col):
        # Check if the same row or diagnals are attacked
        if board[i] == row or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
            return False
    return True


def solve_nqueens(n, col, board, solutions):
    """Solve the N queens problem using backtracking.

    Args:
        n (int): The size of the cheseboard (N).
        col (int): The current column to place a queen.
        board (list): The current state of the board.
        solutions (list): A list to store all valid solutins found.
    """
    if col >= n:
        # A valid solution is found, then append it to the solutions
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i  # Queen is placed
            solve_nqueens(n, col + 1, board, solutions)


def main():
    """Main function to execute the N queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n  # Initialize the board
    solve_nqueens(n, 0, board, solutions)  # Start solving
    print_solutions(solutions)  # Print all solutions


if __name__ == "__main__":
    main()
