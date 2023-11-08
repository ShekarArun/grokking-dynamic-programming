""" 
This program is the naive solution for the Minimum Jumps problem

Problem Statement:
Given an array of positive integers and size n, consider you start at index 0.
Each turn, you can jump anywhere between 1 to array[n] steps.
Find the minimum number of jumps to reach the last index in the array.

eg:
array = [2, 3, 1, 5, 7]
Starting from index 0, the last index can be reached by taking a minimum of 2 jumps:
Take a jump of 1 step, to reach index 1. Then, take a jump of 3 steps to reach index 4.
Therefore, the expected result in this case is 2.

Time Complexity: O(2^n) because for each index, there are n ways to move from one index to another
Space complexity: O(n) as the maximum depth of the recursive chain is n
"""

from inputs import tests
from time import time  # To calculate runtime
from math import inf


def min_jumps(nums: list[int]) -> int:
    return min_jumps_rec(nums, 0)


def min_jumps_rec(nums: list[int], ix: int) -> int:
    n = len(nums)

    if ix >= (n - 1):
        return 0

    jumps = inf

    for i in range((ix + 1), (ix + nums[ix] + 1)):
        jumps = min(jumps, min_jumps_rec(nums, i) + 1)

    return jumps


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
