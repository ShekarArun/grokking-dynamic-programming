""" 
This program is the Bottom-Up (Tabulation) solution for the Count Square Submatrices problem

Problem Statement:
Given a 2D matrix of 0s and 1s, count the number of squares formed by 1s.
Return 0 if the matrix is empty.

eg:
matrix = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0],
]
The expected response in this case is 7

Time Complexity: O(m * n) as we loop over each element in the matrix
Space complexity: O(m * n) as we create a lookup table as the same size as the matrix
"""

from inputs import tests
from time import time  # To calculate runtime


def count_squares(matrix: list[list[int]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    res = 0

    if m == 0 or n == 0:
        return 0

    dp = [[0 for _ in range(n)] for _ in range(m)]

    # As a starting point, copy the first row and column of matrix to the lookup table
    for i in range(m):
        dp[i][0] = matrix[i][0]
    for j in range(n):
        dp[0][j] = matrix[0][j]

    # Iterate over the entire matrix and store the count in the lookup matrix
    for i in range(1, m):
        for j in range(1, n):
            # If the current matrix cell is a 0, no count is to be added
            if matrix[i][j] == 0:
                continue

            # If the cell contains a 1, check the previous cells to see if this extends a square
            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    # Sum up all nonzero values to get the total count
    for i in range(m):
        for j in range(n):
            res += dp[i][j]

    return res


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        matrix = test["matrix"]
        print("=" * 30)
        print("Matrix: ", matrix)
        print("Number of subsquares: ", count_squares(matrix))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
