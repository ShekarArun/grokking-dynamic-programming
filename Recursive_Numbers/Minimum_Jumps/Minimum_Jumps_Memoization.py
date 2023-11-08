""" 
This program is the Top-Down (Memoization) solution for the Minimum Jumps problem

Problem Statement:
Given an array of positive integers and size n, consider you start at index 0.
Each turn, you can jump anywhere between 1 to array[n] steps.
Find the minimum number of jumps to reach the last index in the array.

eg:
array = [2, 3, 1, 5, 7]
Starting from index 0, the last index can be reached by taking a minimum of 2 jumps:
Take a jump of 1 step, to reach index 1. Then, take a jump of 3 steps to reach index 4.
Therefore, the expected result in this case is 2.

Time Complexity: O(n^2) because we take n jumps for each element in the array
Space complexity: O(n) as we use a DP array of size n
"""

from inputs import tests
from time import time  # To calculate runtime
from math import inf


def min_jumps(nums: list[int]) -> int:
    dp = [inf] * (len(nums))
    return min_jumps_rec(nums, 0, dp)


def min_jumps_rec(nums: list[int], ix: int, dp: list[int]) -> int:
    n = len(nums)

    if ix >= (n - 1):
        return 0

    if dp[ix] != inf:
        return dp[ix]

    jumps = inf

    for i in range((ix + 1), (ix + nums[ix] + 1)):
        jumps = min(jumps, min_jumps_rec(nums, i, dp) + 1)

    dp[ix] = jumps
    return dp[ix]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        nums = test["nums"]
        print("=" * 30)
        print("nums: ", nums)
        print("Minimum Jumps: ", min_jumps(nums))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
