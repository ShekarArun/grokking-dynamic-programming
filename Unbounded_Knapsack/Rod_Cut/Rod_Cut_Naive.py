""" 
This program is the naive solution for the Rod Cut problem

Problem Statement:
Given a rod of length 'n' and a set of possible 'sizes' with their corresponding prices, cut the rod in sizes to maximize profit.

eg:
n = 4
sizes = [1, 3, 4]
prices = [2, 7, 8]
The possible cuts are of sizes:
1. [1, 1, 1, 1] -> Total price = 8
2. [1, 3] -> Total price = 9
3. [4] -> Total price = 8
So the maximum revenue earned is 9, with pieces of size 1 and 3.

Time Complexity: O(2^n) because for each size we have a subproblem where we either choose to cut that size or not cut that size
Space complexity: O(n)
"""

from inputs import tests
from time import time  # To calculate runtime


def rod_cut_rec(length: int, sizes: list[int], prices: list[int], n: int) -> int:
    # Base condition to exit from recursive call
    if length == 0 or n == len(sizes):
        # No length remaining
        return 0

    taken = 0
    # Check if the current size's length is less than the remaining capacity
    if sizes[n] <= length:
        # The current item's length is less than the remaining length, so we can choose to either take a cut of that size or not
        taken = prices[n] + rod_cut_rec(length - sizes[n], sizes, prices, n)

    # The item's length is greater than the remaining capacity, so a cut of that length cannot be made
    # OR, it does not maximize profit
    not_taken = rod_cut_rec(length, sizes, prices, n + 1)

    return max(taken, not_taken)


def rod_cut(length: int, sizes: list[int], prices: list[int], n: int) -> int:
    return rod_cut_rec(length, sizes, prices, 0)


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        length = test["length"]
        sizes = test["sizes"]
        prices = test["prices"]
        print("=" * 30)
        print("Length: ", length)
        print("Sizes: ", sizes)
        print("Prices: ", prices)
        print("Max Revenue: ", rod_cut(length, sizes, prices, len(sizes)))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
