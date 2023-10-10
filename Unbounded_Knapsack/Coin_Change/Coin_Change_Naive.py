""" 
This program is the naive solution for the Coin Change Knapsack problem

Problem Statement:
Given a 'total' and a list of integers 'coins'. The integers in the list 'coins' represent the coin denominations, and 'total' is the total amount of money.
Return the minimum number of coins that can make up the 'total' amount by using any combination of the available coins.
Return -1 if the amount can't be made up.
Return 0 if the total is 0.

eg:
total = 5
coins = [1, 2, 3]
The maximum number of coins is 2: 2 + 3 = 5.

Time Complexity: O(n^m) where n is the number of coins and m is the total amount
Space complexity: O(m)
"""

from inputs import tests
from time import time  # To calculate runtime


def coin_change_rec(coins: list[int], total: int, n: int) -> int:
    # Base condition to exit from recursive call
    if total == 0:
        return 0

    if n == 0:
        return -1

    # Check if the current item's weight is less than the remaining capacity
    if coins[n - 1] <= total:
        # Item's weight is lesser than the remaining capacity, so we can choose to either take or not take this item
        taken = coin_change_rec(coins, total - coins[n - 1], n)
        not_taken = coin_change_rec(coins, total, n - 1)

        if taken != -1:
            taken += 1

        if taken == -1:
            return not_taken
        elif not_taken == -1:
            return taken

        # Minimize the result between the two possibilities
        return min(taken, not_taken)
    else:
        # The coin's denomination is greater than the remaining total, so skip it
        return coin_change_rec(coins, total, n - 1)


def coin_change(coins: list[int], total: int) -> int:
    if total == 0:
        return 0

    return coin_change_rec(coins, total, len(coins))


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
