#!/usr/bin/python3
""" text file containing a single character H which can only execute
copy all and paste given a number n"""


def minOperations(n):
    """creates a list of operations with 0 as first element and
    inf->infinity which initialize operations"""
    operations = [0] + [float('inf')] * n
    for i in range(2, n+1):
        for j in range(1, i):
            """check if j is a divisor of i"""
            if i % j == 0:
                """update the value of operations[i] to be the min, then find
                out how many times needed to paste j H's to get i H's"""
                operations[i] = min(operations[i], operations[j] + i // j)
    """return an int, if n is impossible to achieve return 0"""
    return operations[n] if operations[n] < float('inf') else 0
