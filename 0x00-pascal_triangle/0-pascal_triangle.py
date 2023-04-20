#!/usr/bin/python3

"""Module implements pascal triangle"""


def pascal_triangle(n):
    """Function implements pascal traingle"""
    current = []
    result = []
    if n <= 0:
        return []
    for i in range(n + 1):
        if i == 1:
            result.append([1])
        if i == 2:
            result.append([1, 1])
            current.extend([1, 1])
        if i >= 3:
            new = []
            for j in range(len(current)-1):
                new.append(current[j] + current[j+1])
            new.insert(0, 1)
            new.append(1)
            result.append(new)
            current.clear()
            current.extend(new)
    return 
