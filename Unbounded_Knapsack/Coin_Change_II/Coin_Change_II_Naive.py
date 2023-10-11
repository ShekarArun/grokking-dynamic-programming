""" 
This program is the naive solution for the Coin Change II problem

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

Time Complexity: O(n^m) where n is the number of coins and m is the total amount
Space complexity: O(m)
"""

from inputs import tests
from time import time  # To calculate runtime


def count_ways_rec(coins: list[int], total: int, maximum: int) -> int:
    # Base condition to exit from recursive call
    if total == 0:
        return 1
    if total < 0:
        return 0

    res = 0

    for coin in coins:
        if coin <= maximum and (total - coin) >= 0:
            # Maximum is set to current coin in recursive call
            # This ensures we do not duplicate counts (10 + 20 and 20 + 10 should count as only 1 solution)
            res += count_ways_rec(coins, total - coin, coin)

    return res


def count_ways(coins: list[int], total: int) -> int:
    return count_ways_rec(coins, total, max(coins))


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
