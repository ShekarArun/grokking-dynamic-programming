""" 
This program is the Top-Down (Memoization) solution for the Equal Sum Subarrays problem

Problem Statement:
Given an array of positive integers 'arr', determine if it can be divided into two subarrays of equal sum.

eg:
Consider arr = [1, 2, 3]
The array can be divided into two subsets of [1, 2] and [3], both of which add up to 3, so the result is TRUE.

Time Complexity: O(n * target), because for each element we have an option to either take it or leave it
Space Complexity: O(n * target), as we use a dictionary to store the array index and the target sum
"""

from inputs import tests
from time import time  # To calculate runtime


def find_equal_sum_subarrays(arr):
    n = len(arr)
    total = sum(arr)

    # Can only find equal sum if the total is even
    if total % 2 != 0:
        return False

    target = total // 2

    dp = {}
    return find_equal_sum_subarrays_rec(arr, n, target, dp)


def find_equal_sum_subarrays_rec(arr, n, total, dp):
    """
    Logic:
    Parse the complete array moving backwards. Recursively call two possible outputs -> Either taking the current element or skipping it.
    If considering any element to contribute to the total, reduce it from the total so we know how much remainin total is to be achieved
    At any point in a recursive chain, if a solution is already present in the dp array, return that
    """
    # print(n, total)
    # Base condition in case total is achieved
    if total == 0:
        dp[n, total] = True
        return dp[n, total]

    # If we have run out of elements, then we cannot scope further and the total has not been achieved
    # Similarly, if we have exceeded the required total, that is a failed branch as well
    if n == 0 or total < 0:
        dp[n, total] = False
        return dp[n, total]

    # If the solution has already been found, return that
    if (n, total) in dp:
        return dp[n, total]

    # If the current value is greater than the remaining total, it can directly be skipped
    if arr[n - 1] > total:
        dp[n, total] = find_equal_sum_subarrays_rec(arr, n - 1, total, dp)

    # The two possibilities to proceed are to either consider or skip this value in the array
    else:
        dp[n, total] = (find_equal_sum_subarrays_rec(arr, n - 1, total, dp)) or (
            find_equal_sum_subarrays_rec(arr, n - 1, total - arr[n - 1], dp)
        )

    return dp[n, total]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        arr = test["arr"]
        print("=" * 30)
        print("Array: ", arr)
        print("Result: ", find_equal_sum_subarrays(arr))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
