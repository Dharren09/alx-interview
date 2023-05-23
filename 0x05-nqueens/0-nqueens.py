#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """Check if the current position is safe for the queen"""
    for i in range(col):
        """Check if there is a queen in the same row"""
        if board[row][i] == 'Q':
            return False
        """Check if there is a queen in the upper diagonal"""
        if row - i - 1 >= 0 and board[row - i - 1][col - i - 1] == 'Q':
            return False
        """Check if there is a queen in the lower diagonal"""
        if row + i + 1 < len(board) and board[row + i + 1][col - i - 1] == 'Q':
            return False
    return True

def solve_nqueens(board, col):
    n = len(board)
    if col >= n:
        """Found a solution, print the board"""
        print_board(board)
        return
    for row in range(n):
        if is_safe(board, row, col):
            """Place the queen at the current position"""
            board[row][col] = 'Q'
            """Recursively solve for the next column"""
            solve_nqueens(board, col + 1)
            """Backtrack and remove the queen from the current position"""
            board[row][col] = '.'
            
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

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
    board = [['.' for _ in range(n)] for _ in range(n)]
    """Solve the N Queens problem"""
    solve_nqueens(board, 0)

if __name__ == "__main__":
    """Check the number of arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    """Solve the N Queens problem"""
    nqueens(sys.argv[1])
