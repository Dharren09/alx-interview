#!/usr/bin/python3
"""script defines a function that determines the fewest number of coins
needed to meet a given aamount given a pile of coins of different values"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    dip = total
    count_coins = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while dip > 0:
        if coin_idx >= n:
            return -1
        if dip - sorted_coins[coin_idx] >= 0:
            dip -= sorted_coins[coin_idx]
            count_coins += 1
        else:
            coin_idx += 1
    return count_coins
