""" 
This program is the naive solution for the Equal Sum Subarrays problem

Problem Statement:
Given an array of positive integers 'arr', determine if it can be divided into two subarrays of equal sum.

eg:
Consider arr = [1, 2, 3]
The array can be divided into two subsets of [1, 2] and [3], both of which add up to 3, so the result is TRUE.

Time Complexity: O(2^n), because for each element we have an option to either take it or leave it
Space Complexity: O(n), as the recursive call goes up to a maximum depth of n
"""

from inputs import tests
from time import time  # To calculate runtime


def find_equal_sum_subarrays(arr):
    n = len(arr)
    total = sum(arr)

    # Can only find equal sum if the total is even
    if total % 2 != 0:
        return False

    return find_equal_sum_subarrays_rec(arr, n, total // 2)


def find_equal_sum_subarrays_rec(arr, n, total):
    """
    Logic:
    Parse the complete array moving backwards. Recursively call two possible outputs -> Either taking the current element or skipping it.
    If considering any element to contribute to the total, reduce it from the total so we know how much remainin total is to be achieved
    At any point in a recursive chain, if the total is 0, then we have achieved a combination to add up to that value
    """
    # Base condition in case total is achieved
    if total == 0:
        return True

    # If we have run out of elements, then we cannot scope further and the total has not been achieved
    # Similarly, if we have exceeded the required total, that is a failed branch as well
    if n == 0 or total < 0:
        return False

    # If the current value is greater than the remaining total, it can directly be skipped
    if arr[n - 1] > total:
        return find_equal_sum_subarrays_rec(arr, n - 1, total)

    # The two possibilities to proceed are to either consider or skip this value in the array
    return (find_equal_sum_subarrays_rec(arr, n - 1, total)) or (
        find_equal_sum_subarrays_rec(arr, n - 1, total - arr[n - 1])
    )


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
