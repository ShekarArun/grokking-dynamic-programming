""" 
This program is the Bottom-Up (Tabulation) solution for the Subset Sum problem

Problem Statement:
Given an array of positive integers 'arr' and a value 'total', determine if there exists a subset in the given set whose sum adds up to 'total'.

eg:
Consider arr = [1, 2, 3, 7] and T = 6
The subset [1, 2, 3] adds up to 6, so the result is TRUE

Time Complexity: O(n * total), as we loop over every possible total with different subsets of numbers from the list
Space Complexity: O(n * total), as the DP matrix is of those dimensions
"""

from inputs import tests
from time import time  # To calculate runtime


def find_subset_sum(arr, total):
    n = len(arr)
    dp = [[False for _ in range(total + 1)] for _ in range(n + 1)]

    """ 
    Logic:
    Tabulation involves working from the ground up.
    So, for the given input array, consider smaller subsets starting with an empty array
    Then, keep adding elements and see whether introducing it opens up new potential totals 
    """

    for i in range(n + 1):
        for j in range(total + 1):
            # For the initial row, no solution can be obtained due to empty subset (except 0 which is settled in the next condition)
            if i == 0:
                dp[i][j] = False
            # The first column implies a total of '0', which can always be obtained by considering an empty set
            if j == 0:
                dp[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, total + 1):
            # Now for each cell, i indicates the subset considered (rather, the number of elements in the subset -> which implies the first i elements in the set make up the subset)
            # j indicates the total to be obtained
            # So for each cell, identify whether the given column index (total) can be obtained with the given subset defined by i

            # If the current weight is greater than the remaining total, then we can only replicate the same answer as a subset without that element
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

            # Otherwise, it is an OR condition between either taking the element or not
            else:
                dp[i][
                    j
                ] = (  # The previous row same column would have the answer to a subset excluding this element
                    dp[i - 1][j]
                ) or (
                    dp[i - 1][j - arr[i - 1]]
                )  # If the element is considered, then the remaining total reduces to (total - element), so take that to be True or False -> Here, True implies that the remaining total has been obtained through SOME combination of the previous subset (previous because current element cannot add to the total any further), but with a reduced total

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
