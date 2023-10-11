""" 
This program is the Bottom-Up (Tabulation) solution for the Coin Change II problem

Problem Statement:
Given a 'total' and a list of integers 'coins'. The integers in the list 'coins' represent the coin denominations, and 'total' is the total amount of money.
Return the number of ways in which the provided coins can add up to the given amount.
Return 0 if there is no possible way to represent the total with the given denominations.
Return 0 if the total is 0.

eg:
total = 30
coins = [10, 20]
The following combinations are possible:
1. 10 + 20
2. 10 + 10 + 10
So the expected response is 2.

Time Complexity: O(m * n) where n is the number of coins and m is the total amount
Space complexity: O(m * n)
"""

from inputs import tests
from time import time  # To calculate runtime


def count_ways(coins: list[int], total: int) -> int:
    if total == 0:
        return 1
    if total < 0:
        return 0

    dp = [[1 for _ in range(len(coins))] for _ in range(total + 1)]

    for val in range(1, total + 1):
        for j in range(len(coins)):
            coin = coins[j]
            if val - coin >= 0:
                x = dp[val - coin][j]
            else:
                x = 0

            if j >= 1:
                y = dp[val][j - 1]
            else:
                y = 0

            dp[val][j] = x + y

    return dp[-1][-1]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        coins = test["coins"]
        total = test["total"]
        print("=" * 30)
        print("Coins: ", coins)
        print("Total: ", total)
        print("Number of ways: ", count_ways(coins, total))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
