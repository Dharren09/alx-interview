#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    """Check if the current position is safe for the queen"""
    for i in range(col):
        """Check if there is a queen in the same row"""
        if board[i] == row:
            return False
        """Check if there is a queen in the upper diagonal"""
        if board[i] == row - (col - i) or board[i] == row + (col - i):
            return False
    return True


def solve_nqueens(board, col, n, solutions):
    if col >= n:
        """Found a solution, add it to the list of solutions"""
        solutions.append(list(board))
        return
    for row in range(n):
        if is_safe(board, row, col):
            """Place the queen at the current position"""
            board[col] = row
            """Recursively solve for the next column"""
            solve_nqueens(board, col + 1, n, solutions)
            """Backtrack and remove the queen from the current position"""
            board[col] = -1


def nqueens(n):
    """Check if N is an integer"""
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    """Check if N is at least 4"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    """Initialize the board"""
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(n)]
        print(formatted_solution)


if __name__ == "__main__":
    """Check the number of arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
