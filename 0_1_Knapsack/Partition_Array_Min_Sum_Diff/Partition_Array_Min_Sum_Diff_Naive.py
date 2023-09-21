""" 
This program is the naive solution for the Partition Array for Min Sum Difference problem

Problem Statement:
Given an array of positive integers 'arr', partition the array into two arrays such that the absolute difference between their sums is minimized.

eg:
Consider arr = [1, 2, 3]
The array can be partitioned into [1, 2] and [3], such that the sums of the two arrays are 3 and 3. So, the absolute difference is 3 - 3 = 0

Time Complexity: O(2^n), because for each element we have an option to either take it or leave it
Space Complexity: O(n), as the recursive call goes up to a maximum depth of n
"""

from inputs import tests
from time import time  # To calculate runtime


def min_partition_arr_sum_diff(arr):
    return min_partition_arr_sum_diff_helper(arr, 0, 0, 0)


def min_partition_arr_sum_diff_helper(arr, i, sum1, sum2):
    """
    Logic:
    The naive solution involves building every combination of two arrays possible for the given input array.
    Then, obtaining the minimum difference between the two.
    This can be achieved by taking the minimum value returned between the two subproblems - One where the current element is taken into the first array, and another where it is taking into the second array.
    """
    # Base condition: If i reaches the length of the array, there are no more elements to process
    # So obtain the difference between the two sums and return it.
    if i == len(arr):
        return abs(sum1 - sum2)

    # Otherwise, we can build the two possible subproblems and return the minimum difference between the two
    return min(
        min_partition_arr_sum_diff_helper(arr, i + 1, sum1 + arr[i], sum2),
        min_partition_arr_sum_diff_helper(arr, i + 1, sum1, sum2 + arr[i]),
    )


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
