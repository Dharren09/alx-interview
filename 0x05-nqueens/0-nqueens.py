#!/usr/bin/python3
"""N queens module"""
import sys


def get_input():
    """Get input from command line"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    return n


def queens(n, i, a, b, c):
    """Recursive function to solve N-Queens problem"""
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


if __name__ == '__main__':
    n = get_input()
    for solution in queens(n, 0, [], [], []):
        print([[i, j] for i, j in enumerate(solution)])
