""" 
This program is the Top-Down (Memoization) solution for the Target Sum problem

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

Time Complexity: O(n * sum(arr)), Calculated answers are present in the lookup so we have a worst case complexity of n numbers in the array times every sum combination possible
Space Complexity: O(n * sum(arr)), This is the size of the DP array created
"""

from inputs import tests
from time import time  # To calculate runtime


def find_target_sum_ways(arr, T):
    total = sum(arr)

    # If the unsigned numbers do not add up to Target, then there is no possible solution
    if total < abs(T):
        return 0

    dp = [[0] * ((2 * total) + 1) for _ in range(len(arr))]

    # Taking the first variable of the array, find its distance +- from the total sum
    # Increment these values to 1, as that implies that the particular column value can be obtained by applying arr[0] on target
    dp[0][total + arr[0]] = 1
    # +=1 because if target is 0 then this cell has 2 possible ways to be calculated (+0 and -0)
    dp[0][total - arr[0]] += 1

    # Start from second element in array
    for i in range(1, len(arr)):
        for t in range(-total, total + 1):
            if not dp[i][t]:
                # This means so far some combinations have resulted in this column value (as the target)
                # So to the ne
                pass  # TODO: Build upon this logic


def find_target_sum_ways_rec(arr, i, T, dp):
    # If all integers in the array have been processed
    if i == len(arr):
        # If the target has been reached
        if T == 0:
            return 1
        # Otherwise, target has not been reached
        return 0

    if dp[i][T] != -1:
        return dp[i][T]

    # Calculate both subproblems and store result in memory
    dp[i][T] = find_target_sum_ways_rec(
        arr, i + 1, T + arr[i], dp
    ) + find_target_sum_ways_rec(arr, i + 1, T - arr[i], dp)

    # print("i", i, "T", T, "dp", dp)

    return dp[i][T]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        arr = test["arr"]
        T = test["total"]
        print("=" * 30)
        print("Array: ", arr)
        print("Total: ", T)
        print("Number of expressions: ", find_target_sum_ways(arr, T))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
