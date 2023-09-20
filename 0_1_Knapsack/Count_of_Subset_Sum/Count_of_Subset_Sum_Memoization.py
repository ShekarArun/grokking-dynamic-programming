""" 
This program is the Top-Down (Memoization) solution for the Count of Subset Sum problem

Problem Statement:
Given an array of positive integers 'arr' and a value 'total', determine the number of subsets in the given set whose sum adds up to 'total'.

eg:
Consider arr = [1, 2, 3, 4] and T = 4
The subsets [1, 3] and [4] adds up to 6, so the result is 2

Time Complexity: O(n * total), as we loop over every possible total with different subsets of numbers from the list
Space Complexity: O(n * total), as the DP matrix is of those dimensions
"""

from inputs import tests
from time import time  # To calculate runtime


def find_subset_sum(arr, total):
    n = len(arr)
    dp = [[-1 for _ in range(total + 1)] for _ in range(n + 1)]
    return find_subset_sum_rec(arr, n, total, dp)


def find_subset_sum_rec(arr, n, total, dp):
    """
    Logic:
    Memoization involves working backwards from the initial problem set.
    Consider the entire array, and see if each element can potentially contribute to the solution.
    If yes, then check whether that subproblem has a solution already calculated, and return if so.
    Otherwise, proceed to find the solution for that subproblem and store for future reference.
    """
    # Base condition in case total is achieved
    if total == 0:
        return 1

    # If we have run out of elements, then we cannot scope further and the total has not been achieved
    if n == 0 or total < 0:
        return 0

    # Check if a solution has already been obtained for the given subproblem
    if dp[n][total] != -1:
        return dp[n][total]

    # If the current value is greater than the remaining total, it can directly be skipped
    if arr[n - 1] > total:
        dp[n][total] = find_subset_sum_rec(arr, n - 1, total, dp)

    # The two possibilities to proceed are to either consider or skip this value in the array
    dp[n][total] = (find_subset_sum_rec(arr, n - 1, total, dp)) + (
        find_subset_sum_rec(arr, n - 1, total - arr[n - 1], dp)
    )

    return dp[n][total]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        arr = test["arr"]
        total = test["total"]
        print("=" * 30)
        print("Array: ", arr)
        print("Total: ", total)
        print("Result: ", find_subset_sum(arr, total))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
