#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same row
    if any(board[row][c] == 1 for c in range(col)):
        return False

    # Check upper diagonal on left side
    if any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    # Check lower diagonal on left side
    if any(board[i][j] == 1 for i, j in zip(range(row, N), range(col, -1, -1))):
        return False

    return True

def solve_nqueens(N, board, col, solutions):
    if col == N:
        solutions.append([i[:] for i in board])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(N, board, col + 1, solutions)
            board[i][col] = 0  # Backtrack

def print_solutions(solutions):
    for sol in solutions:
        print(sol)

def nqueens(N):
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
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
