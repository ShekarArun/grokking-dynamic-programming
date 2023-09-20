""" 
This program is the Bottom-Up (Tabulation) solution for the Count of Subset Sum problem

Problem Statement:
Given an array of positive integers 'arr' and a value 'total', determine the count of subsets in the given set whose sum adds up to 'total'.

eg:
Consider arr = [1, 2, 3, 4] and T = 4
The subsets [1, 3] and [4] add up to 4, so the result is 2

Time Complexity: O(n * total), as we loop over every possible total with different subsets of numbers from the list
Space Complexity: O(n * total), as the DP matrix is of those dimensions
"""

from inputs import tests
from time import time  # To calculate runtime


def find_subset_sum(arr, total):
    n = len(arr)
    dp = [[0 for _ in range(total + 1)] for _ in range(n + 1)]

    """ 
    Logic:
    Tabulation involves working from the ground up.
    So, for the given input array, consider smaller subsets starting with an empty array
    Then, keep adding elements and see whether introducing it opens up new potential totals 
    """

    for i in range(n + 1):
        for j in range(total + 1):
            # Now for each cell, i indicates the subset considered (rather, the number of elements in the subset -> which implies the first i elements in the set make up the subset)
            # j indicates the total to be obtained
            # So for each cell, identify whether the given column index (total) can be obtained with the given subset defined by i

            if i == 0:
                # Without considering any elements, we can't obtain any sum, except 0 which is adjusted in the next IF block
                dp[i][j] = 0

            if j == 0:
                # A total of 0 can always be obtained only once -> By considering no elements (i.e. Empty set)
                dp[i][j] = 1

            # If the current weight is greater than the remaining total, then we can only replicate the same answer as a subset without that element
            elif arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

            # Otherwise, it is the sum of solutions where we either take the element or not
            else:
                # dp[i - 1][j] -> The previous row same column would have the answer to a subset excluding this element
                # dp[i - 1][j - arr[i - 1]] -> If the element is considered, then the remaining total reduces to (total - element), so take that value to add to the number of subsets contributing to solution
                dp[i][j] = (dp[i - 1][j]) + (dp[i - 1][j - arr[i - 1]])

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
