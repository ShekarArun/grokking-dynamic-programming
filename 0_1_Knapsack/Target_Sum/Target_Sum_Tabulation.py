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

Time Complexity: O(n * sum(arr))
Space Complexity: O(n * sum(arr)), This is the size of the DP array created

Note:
- Can optimize space complexity to be O(capacity) by taking a 2 row array to store intermediate values, as we always only need the current row and previous row
"""

from inputs import tests
from time import time  # To calculate runtime


def find_target_sum_ways(arr, T):
    total = sum(arr)

    # If the unsigned numbers do not add up to Target, then there is no possible solution
    if total < abs(T):
        return 0

    dp = [[0 for _ in range((2 * total) + 1)] for _ in range(len(arr))]

    # Taking the first variable of the array, find its distance +- from the total sum
    # Increment these values to 1, as that implies that the particular column value can be obtained by applying arr[0] on target
    dp[0][total + arr[0]] = 1
    # +=1 because if target is 0 then this cell has 2 possible ways to be calculated (+0 and -0)
    dp[0][total - arr[0]] += 1

    # print(dp)
    # Start from second element in array
    for i in range(1, len(arr)):
        for t in range(-total, total + 1):
            # Notice how for all column values we're taking total + t
            # This is to ensure We start off from a '0' index for the column value
            # Because we're ranging from -total to total
            if dp[i - 1][total + t] != 0:
                # This means so far some combinations have resulted in this column value (as the target)
                # So to the next value has to be further propagated to values +- this target
                dp[i][total + t + arr[i]] += dp[i - 1][total + t]
                dp[i][total + t - arr[i]] += dp[i - 1][total + t]
    # print(dp)
    return dp[-1][total + T]


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
