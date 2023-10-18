""" 
This program is the naive solution for the Unique Paths to Goal problem

Problem Statement:
Given a robot located at the top left corner of an M x N matrix, determine the number of unique paths it can take to reach the bottom-right of the matrix. The matrix is denoted by 0s and the 1s indicate obstacles which are cells the robot cannot move to.
The robot can only move down or right at a time.

eg:
matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
The different moves that can be made are:
1. R + R + D + D
2. D + D + R + R
Unique Paths: 2

Time Complexity: O(2^(m*n)) as for each matrix there are 2 possible moves -> Right or Down, and the matrix has m*n cells
Space complexity: O(m*n)
"""

from inputs import tests
from time import time  # To calculate runtime


def find_unique_paths(matrix: list[list[int]]) -> int:
    r = len(matrix)
    c = len(matrix[0])

    return find_unique_paths_rec(0, 0, r, c, matrix)


def find_unique_paths_rec(
    i: int, j: int, r: int, c: int, matrix: list[list[int]]
) -> int:
    # Exit if we have reached an outer limit
    if i == r or j == c:
        return 0

    # Exit if we hit an obstacle
    if matrix[i][j] == 1:
        return 0

    # Return as one possible route if we reach the bottom-right corner
    if i == (r - 1) and j == (c - 1):
        return 1

    return find_unique_paths_rec(i + 1, j, r, c, matrix) + find_unique_paths_rec(
        i, j + 1, r, c, matrix
    )


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        matrix = test["matrix"]
        print("=" * 30)
        print("Matrix: ", matrix)
        print("Unique Paths to Goal: ", find_unique_paths(matrix))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
