#!/usr/bin/python3
"""script defines a function that determines the fewest number of coins
needed to meet a given aamount given a pile of coins of different values"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    """initialize a list to store the minimum number of coins"""
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    """iterate through all possible totals"""
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
