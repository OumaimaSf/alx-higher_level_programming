#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if placing a queen in the given position is safe.

    Args:
    - board: The current state of the chessboard.
    - row: The row where the queen is to be placed.
    - col: The column where the queen is to be placed.
    - N: The size of the chessboard.

    Returns:
    - True if it's safe to place a queen, False otherwise.
    """
    if any(board[row][c] == 1 for c in range(col)):
        return False

    if any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    if any(board[i][j] == 1 for i, j in zip(range(row, N), range(col, -1, -1))):
        return False

    return True

def solve_nqueens(N, board, col, solutions):
    """
    Recursively find all solutions to the N-Queens problem.

    Args:
    - N: The size of the chessboard.
    - board: The current state of the chessboard.
    - col: The current column being considered.
    - solutions: List to store the found solutions.
    """
    if col == N:
        solutions.append([i[:] for i in board])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(N, board, col + 1, solutions)
            board[i][col] = 0  # Backtrack

def print_solutions(solutions):
    """
    Print the found N-Queens solutions.

    Args:
    - solutions: List of solutions to be printed.
    """
    for sol in solutions:
        print(sol)

def nqueens(N):
    """
    Validate input and find solutions for the N-Queens problem.

    Args:
    - N: The size of the chessboard.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_nqueens(N, board, 0, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    """
    Check command-line arguments and execute the program.
    """
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
