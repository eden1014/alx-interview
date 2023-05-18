#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''



def makeChange(coins, total):
    ''' 
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''

    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
