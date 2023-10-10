""" 
This program is the Bottom-Up (Tabulation) solution for the Coin Change problem

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
Space complexity: O(m)
"""

from inputs import tests
from time import time  # To calculate runtime
from math import inf


def coin_change(coins: list[int], total: int) -> int:
    if total == 0:
        return 0

    dp = [(total + 1)] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if (i - coin) >= 0:
                dp[i] = min(dp[i], (1 + dp[i - coin]))

    if dp[total] != (total + 1):
        return dp[total]
    else:
        return -1


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
