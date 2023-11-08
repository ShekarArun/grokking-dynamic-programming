""" 
This program is the Bottom-Up (Tabulation) solution for the Minimum Jumps problem

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
    n = len(nums)
    dp = [inf] * (len(nums))
    dp[0] = 0

    # Outer loop traverses each element in the array
    for i in range(1, n):
        # Inner loop traverses the values from start up to the current element
        for j in range(i):
            # Check if the current element can be reached from j position
            # This is possible if Jth index + J is greater than i, and Jth element is not infinity (i.e. not reachable)
            if ((i <= nums[j] + j)) and (dp[j] != inf):
                # Update count of jumps to minimum value between current, and one jump from Jth position
                dp[i] = min(dp[i], dp[j] + 1)
                break

    return dp[-1]


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
