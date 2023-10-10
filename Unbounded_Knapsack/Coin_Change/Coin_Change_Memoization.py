""" 
This program is the Top-Down (Memoization) solution for the Coin Change problem

Problem Statement:
Given a 'total' and a list of integers 'coins'. The integers in the list 'coins' represent the coin denominations, and 'total' is the total amount of money.
Return the minimum number of coins that can make up the 'total' amount by using any combination of the available coins.
Return -1 if the amount can't be made up.
Return 0 if the total is 0.

eg:
total = 5
coins = [1, 2, 3]
The maximum number of coins is 2: 2 + 3 = 5.

Time Complexity: O(n*m) where n is the number of coins and m is the total amount
Space complexity: O(n*m)
"""

from inputs import tests
from time import time  # To calculate runtime
from math import inf


def coin_change_rec(coins: list[int], total: int, dp: list[int]) -> int:
    # Base condition to exit from recursive call
    if total == 0:
        return 0

    if total < 0:
        return -1

    if dp[total - 1] != inf:
        return dp[total - 1]

    minimum = inf

    for coin in coins:
        res = coin_change_rec(coins, total - coin, dp)
        # Only add valid solutions, do not consider if the denominations don't add up to total
        if res >= 0 and res < minimum:
            minimum = 1 + res

    if minimum != inf:
        dp[total - 1] = minimum
        return dp[total - 1]
    else:
        return -1


def coin_change(coins: list[int], total: int) -> int:
    if total == 0:
        return 0

    dp = [inf] * total

    return coin_change_rec(coins, total, dp)


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        coins = test["coins"]
        total = test["total"]
        print("=" * 30)
        print("Coins: ", coins)
        print("Total: ", total)
        print("Min Coins: ", coin_change(coins, total))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
