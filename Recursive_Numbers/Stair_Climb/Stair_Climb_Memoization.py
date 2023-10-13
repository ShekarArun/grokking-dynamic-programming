""" 
This program is the naive solution for the Staircase Climb problem

Problem Statement:
A child is climbing a staircase and can climb 1, 2 or 3 steps at a time.
Find the number of ways in which the staircase can be climbed.

eg:
n = 3
The different ways are:
1. 1 + 1 + 1
2. 1 + 2
3. 2 + 1
4. 3

Time Complexity: O(3^n) because there are 3 possible options at each step
Space complexity: O(n) as the maximum depth of the recursive chain is n
"""

from inputs import tests
from time import time  # To calculate runtime


def stair_climb(n: int) -> int:
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return stair_climb(n - 1) + stair_climb(n - 2) + stair_climb(n - 3)


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        n = test["n"]
        print("=" * 30)
        print("n: ", n)
        print("Number of ways: ", stair_climb(n))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
