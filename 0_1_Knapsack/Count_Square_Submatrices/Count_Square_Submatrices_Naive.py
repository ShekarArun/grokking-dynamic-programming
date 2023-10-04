""" 
This program is the naive solution for the Count Square Submatrices problem

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

Time Complexity: O(2^n) because for each weight we have a subproblem where we either choose or do not choose it
Space complexity: O(n)
"""

from inputs import tests
from time import time  # To calculate runtime


def count_squares(matrix: list[list[int]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    res = 0

    # Iterate over the entire matrix
    for i in range(m):
        for j in range(n):
            # If the cell contains a 1, traverse further to find the largest square possible from here
            if matrix[i][j] == 1:
                res += count_squares_rec(matrix, i, j, m, n)

    return res


def count_squares_rec(matrix: list[list[int]], i: int, j: int, m: int, n: int) -> int:
    # If we go out of range, end the recursive call with 0 more values to add
    if i >= m or j >= n or matrix[i][j] == 0:
        return 0

    right = count_squares_rec(matrix, i, j + 1, m, n)
    bottom = count_squares_rec(matrix, i + 1, j, m, n)
    bottom_right = count_squares_rec(matrix, i + 1, j + 1, m, n)

    # Adding 1 to return value to account for current cell itself being a square
    return 1 + min(right, bottom, bottom_right)


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
