""" 
This program is the Bottom-Up (Tabulation) solution for the Rod Cut problem

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

Time Complexity: O(n * k) where n is the length of the rod and k is the number of possible lengths
Space complexity: O(n * k)
"""

from inputs import tests
from time import time  # To calculate runtime


def rod_cut(length: int, sizes: list[int], prices: list[int]) -> int:
    num_sizes = len(sizes)
    num_prices = len(prices)

    if length == 0 or num_prices == 0 or num_prices != num_sizes:
        return 0

    dp = [[0 for _ in range(length + 1)] for _ in range(num_sizes)]

    for size_idx in range(num_sizes):
        for rod_length in range(1, length + 1):
            taken = not_taken = 0
            if sizes[size_idx] <= rod_length:
                taken = prices[size_idx] + dp[size_idx][rod_length - sizes[size_idx]]
            if size_idx > 0:
                not_taken = dp[size_idx - 1][rod_length]

            dp[size_idx][rod_length] = max(taken, not_taken)

    return dp[num_sizes - 1][length]


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
        print("Max Revenue: ", rod_cut(length, sizes, prices))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
