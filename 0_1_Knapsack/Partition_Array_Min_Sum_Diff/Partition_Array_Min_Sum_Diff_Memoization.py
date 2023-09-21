""" 
This program is the Top-Down (Memoization) solution for the Partition Array for Min Sum Difference problem

Problem Statement:
Given an array of positive integers 'arr', partition the array into two arrays such that the absolute difference between their sums is minimized.

eg:
Consider arr = [1, 2, 3]
The array can be partitioned into [1, 2] and [3], such that the sums of the two arrays are 3 and 3. So, the absolute difference is 3 - 3 = 0

Time Complexity: O(n * S), where S is the sum of all elements in the input array
Space Complexity: O(n * S), where S is the sum of all elements in the input array
"""

from inputs import tests
from time import time  # To calculate runtime


def min_partition_arr_sum_diff(arr):
    dp = [[-1 for _ in range(sum(arr) + 1)] for _ in range(len(arr))]
    res = min_partition_arr_sum_diff_helper(arr, 0, 0, 0, dp)
    print(dp)
    return res


def min_partition_arr_sum_diff_helper(arr, i, sum1, sum2, dp):
    """
    Logic:
    The memoization solution involves building every combination of two arrays possible for the given input array.
    Then, obtaining the minimum difference between the two.
    This can be achieved by taking the minimum value returned between the two subproblems - One where the current element is taken into the first array, and another where it is taking into the second array.
    It upgrades on the naive solution by storing a solution in the DP array, against the value of i and sum1. For any given sum1, the sum2 remains the same so we need not store its value.
    """
    # Base condition: If i reaches the length of the array, there are no more elements to process
    # So obtain the difference between the two sums and return it.
    if i == len(arr):
        return abs(sum1 - sum2)

    # Otherwise, we can build the two possible subproblems and return the minimum difference between the two
    if dp[i][sum1] != -1:
        return dp[i][sum1]
    else:
        dp[i][sum1] = min(
            min_partition_arr_sum_diff_helper(arr, i + 1, sum1 + arr[i], sum2, dp),
            min_partition_arr_sum_diff_helper(arr, i + 1, sum1, sum2 + arr[i], dp),
        )
        return dp[i][sum1]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        arr = test["arr"]
        print("=" * 30)
        print("Array: ", arr)
        print("Result: ", min_partition_arr_sum_diff(arr))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
