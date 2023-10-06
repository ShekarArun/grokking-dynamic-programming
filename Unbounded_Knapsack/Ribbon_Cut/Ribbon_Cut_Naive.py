""" 
This program is the naive solution for the Ribbon Cut problem

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

Time Complexity: O(2^n) because for each size we have a subproblem where we either choose to cut that size or not cut that size
Space complexity: O(n)
"""

from inputs import tests
from time import time  # To calculate runtime


def ribbon_cut_rec(length: int, sizes: list[int], n: int) -> int:
    # Base condition to exit from recursive call
    if length == 0:
        # No length remaining
        return 0

    if n < 0:
        # We've exhausted all possibilities and not reached the desired length
        return -1

    # Check if the current size's length is less than the remaining capacity
    if sizes[n] <= length:
        # The current item's length is less than the remaining length, so we can choose to either take a cut of that size or not
        taken = ribbon_cut_rec(length - sizes[n], sizes, n)
        if taken != -1:
            taken += 1  # Add 1 for the remaining piece after all cuts are done
        not_taken = ribbon_cut_rec(length, sizes, n - 1)

        # Maximize the number of pieces obtained between the two possibilities
        return max(taken, not_taken)
    else:
        # The item's length is greater than the remaining capacity, so a cut of that length cannot be made
        return ribbon_cut_rec(length, sizes, n - 1)


def ribbon_cut(length: int, sizes: list[int], n: int) -> int:
    return ribbon_cut_rec(length, sizes, n - 1)


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
