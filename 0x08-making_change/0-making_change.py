def makeChange(coins, total):
    if total <= 0:
        return 0

    # initialize the list with a large value for each index, except for the first index
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # iterate over the coin values and the indices in the list
    for coin in coins:
        for i in range(coin, total + 1):
            # update the list at index i
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # return the value at the index of the total
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
