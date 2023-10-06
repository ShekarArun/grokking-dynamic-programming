""" 
This program is the Bottom-Up (Tabulation) solution for the Ribbon Cut problem

Problem Statement:
Given a ribbon of length 'n' and a set of possible 'sizes', cut the ribbon in sizes such that the 'n' is achieved with the maximum number of pieces.
If 'n' can't be made up, return -1.

eg:
n = 13
sizes = [5, 3, 8]
The possible cuts are:
1. [5, 8]
2. [5, 5, 3]
The expected result is '3' as that is the maximum number of pieces we can obtain.

Time Complexity: O(n * k) where n is the length of the ribbon and k is the number of sizes possible
Space complexity: O(n) where n is the length of the ribbon
"""

from inputs import tests
from time import time  # To calculate runtime


def ribbon_cut(length: int, sizes: list[int]) -> int:
    dp = [-1] * (length + 1)
    dp[0] = 0  # Can't get any pieces for length 0

    # Intuition is that we obtain the max pieces for each length incrementally
    # If a size is within a particular length, then the max pieces without that size + 1 will give the current max pieces
    for i in range(1, length + 1):
        for size in sizes:
            if i - size >= 0 and dp[i - size] != -1:
                dp[i] = max(dp[i], 1 + dp[i - size])

    return dp[length]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        length = test["length"]
        sizes = test["sizes"]
        print("=" * 30)
        print("Length: ", length)
        print("Sizes: ", sizes)
        print("Max Pieces: ", ribbon_cut(length, sizes))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
