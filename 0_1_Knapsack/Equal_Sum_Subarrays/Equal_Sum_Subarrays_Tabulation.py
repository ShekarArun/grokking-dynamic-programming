""" 
This program is the Bottom-Up (Tabulation) solution for the Equal Sum Subarrays problem

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
    """
    Logic:
    Build a DP array of dimensions n * (total // 2) with False values as default.
    Rows represent the number of items taken into the collection. Columns represent the total achieved.
    If a particular column value can be achieved, set it to True.
    """
    n = len(arr)
    total = sum(arr)

    # Can only find equal sum if the total is even
    if total % 2 != 0:
        return False

    # Floor division performed to obtain int result for comparison
    target = total // 2

    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

    # None of the targets (except 0) will be achievable in the first row as row index 0 implies none of the elements are taken into consideration
    for i in range(target + 1):
        dp[0][i] = False

    # Target 0 is achievable with any combination of elements
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] > j:
                # Target cannot be achieved with the current element, so just copy the result from the previous subset
                dp[i][j] = dp[i - 1][j]
            else:
                # Target may potential be achieved either by taking this element or by skipping it
                # If we take the element, the remaining target would've been achieved by the value of current column - array element, which would be present in (current column - array element)
                # Or, we skip it, the solution for which would be in the same column but with the previous subset
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]

    return dp[-1][-1]


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
