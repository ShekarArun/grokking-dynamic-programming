""" 
This program is the Top-Down (Memoization) solution for the Ribbon Cut problem

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
Space complexity: O(n * k) where n is the length of the ribbon and k is the number of sizes possible
"""

from inputs import tests
from time import time  # To calculate runtime


def ribbon_cut_rec(length: int, sizes: list[int], n: int, dp: list[list[int]]) -> int:
    # Base condition to exit from recursive call
    if length == 0:
        # No length remaining
        return 0

    if n < 0:
        # We've exhausted all possibilities and not reached the desired length
        return -1

    # If the answer has been solved previously, return that
    if dp[n][length] != -1:
        return dp[n][length]

    # Check if the current size's length is less than the remaining capacity
    if sizes[n] <= length:
        # The current item's length is less than the remaining length, so we can choose to either take a cut of that size or not
        taken = ribbon_cut_rec(length - sizes[n], sizes, n, dp)
        if taken != -1:
            taken += 1  # Add 1 for the remaining piece after all cuts are done
        not_taken = ribbon_cut_rec(length, sizes, n - 1, dp)

        # Maximize the number of pieces obtained between the two possibilities
        dp[n][length] = max(taken, not_taken)
    else:
        # The item's length is greater than the remaining capacity, so a cut of that length cannot be made
        dp[n][length] = ribbon_cut_rec(length, sizes, n - 1, dp)

    return dp[n][length]


def ribbon_cut(length: int, sizes: list[int], n: int) -> int:
    dp = [[-1 for _ in range(length + 1)] for _ in range(n)]
    return ribbon_cut_rec(length, sizes, n - 1, dp)


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        length = test["length"]
        sizes = test["sizes"]
        print("=" * 30)
        print("Length: ", length)
        print("Sizes: ", sizes)
        print("Max Pieces: ", ribbon_cut(length, sizes, len(sizes)))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
