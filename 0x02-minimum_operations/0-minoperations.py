#!/usr/bin/python3

# This is a function that takes an integer n and returns the minimum
# number of operations needed to obtain n H's in a text file, given that
# the only operations allowed are copy all and paste.

def minOperations(n):
    
    # Check if n is an integer; if not, return 0
    if not isinstance(n, int):
        return 0
    
    # Set up a counter for operations and an iterator starting from 2
    operations = 0
    iterator = 2
    
    # While the iterator is less than or equal to n, check if n is
    # divisible by the iterator. If it is, divide n by the iterator,
    # add the value of the iterator to the operations counter, and
    # reset the iterator to 1 to start checking from the beginning.
    # If it's not divisible, increment the iterator by 1 and continue.
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    
    # Return the operations counter
    return operations
