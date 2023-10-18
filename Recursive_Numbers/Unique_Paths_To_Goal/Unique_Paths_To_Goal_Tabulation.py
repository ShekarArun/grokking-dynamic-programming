""" 
This program is the Bottom-Up (Tabulation) solution for the Unique Paths to Goal problem

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

Time Complexity: O(m*n) as we calculate the solution of each matrix cell once
Space complexity: O(1) as we do not need any auxiliary space
"""

from inputs import tests
from time import time  # To calculate runtime


def find_unique_paths(matrix: list[list[int]]) -> int:
    r = len(matrix)
    c = len(matrix[0])

    # If the starting cell has an obstacle, no solution can be obtained
    if matrix[0][0] == 1:
        return 0

    # The first cell can be reached in 1 way
    matrix[0][0] = 1

    # Fill the first column based on top left cell values
    for i in range(1, r):
        matrix[i][0] = int(matrix[i][0] == 0 and matrix[i - 1][0] == 1)

    # Similarly, fill the first row based on top left cell values
    for j in range(1, c):
        matrix[0][j] = int(matrix[0][j] == 0 and matrix[0][j - 1] == 1)

    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
            else:
                # This means there is an obstacle in this cell, so no way to reach this cell
                matrix[i][j] = 0

    return matrix[-1][-1]


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
