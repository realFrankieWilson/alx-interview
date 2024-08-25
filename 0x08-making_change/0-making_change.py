#!/usr/bin/python3
"""A function that determin the fewest number of coins needed
to meet a given amount total.
Args:
  coins: List of the values of the coins in possesion
  total: The expected total coin
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the minimm coins needed for each amount.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0    # Base case: 0 coins are needed to make the total of 0

    # Iterate over each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    # If dp[total] is still infinity, it means we cannot make the total
    return dp[total] if dp[total] != float('inf') else -1
