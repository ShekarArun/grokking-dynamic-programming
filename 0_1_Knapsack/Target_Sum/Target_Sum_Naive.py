""" 
This program is the naive solution for the Target Sum problem

Problem Statement:
Given an array of positive integers 'arr' and a target 'T', build an expression using these numbers by inserting a '+' or a '-' before each integer, and evaluating the expression.
Find the total number of different expressions that evaluate to 'T'.

eg:
Consider arr = [1, 1] and T = 0
We can build the following expressions:
[+1, +1] => Total = 2
[+1, -1] => Total = 0
[-1, +1] => Total = 0
[-1, -1] => Total = -2

Time Complexity: O(2^n), because for each element we have an option to either take it as + or -
Space Complexity: O(n), as the recursive call goes up to a maximum depth of n
"""

from inputs import tests
from time import time  # To calculate runtime


def find_target_sum_ways(arr, total):
    sol = find_target_sum_ways_rec(arr, 0, total)
    return sol


def find_target_sum_ways_rec(arr, i, total):
    # If all integers in the array have been processed
    if i == len(arr):
        # If the target has been reached
        if total == 0:
            return 1
        # Otherwise, target has not been reached
        return 0

    # Return the total of subproblems
    # Subproblems are such that we either add or subtract the current element from the target
    # Eat away at the target value until we reach 0 -> Then, that is a valid expression
    return (
        # Note: Adding to total implies we are taking the integer to be negative
        find_target_sum_ways_rec(arr, i + 1, total + arr[i])
        + find_target_sum_ways_rec(arr, i + 1, total - arr[i])
    )


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        arr = test["arr"]
        total = test["total"]
        print("=" * 30)
        print("Array: ", arr)
        print("Total: ", total)
        print("Number of expressions: ", find_target_sum_ways(arr, total))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
