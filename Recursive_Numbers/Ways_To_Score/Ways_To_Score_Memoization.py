""" 
This program is the Top-Down (Memoization) solution for the Number of Ways to Score in a Game problem

Problem Statement:
Given a list of possible points and a target score 'n', find the number of ways in which points can be scored to achieve the desired total.

eg:
n = 3
numbers = [1, 2, 4]
The different ways to score the desired total are:
1. 1 + 1 + 1
2. 1 + 2
3. 2 + 1
So the expected result is '3'.

Time Complexity: O(n) as the solution for a given number up to n is calculated only once
Space complexity: O(n) as we use a DP array of size n
"""

from inputs import tests
from time import time  # To calculate runtime


def count_ways_rec(n: int, numbers: list[int], dp: list[int]) -> int:
    if n < 0:
        return 0

    if n == 0:
        return 1

    if dp[n] != -1:
        return dp[n]

    res = 0

    for number in numbers:
        res += count_ways_rec((n - number), numbers, dp)

    dp[n] = res
    return dp[n]


def count_ways(n: int, numbers: list[int]) -> int:
    dp = [-1] * (n + 1)
    return count_ways_rec(n, numbers, dp)


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        n = test["n"]
        numbers = test["numbers"]
        print("=" * 30)
        print("n: ", n)
        print("Numbers: ", numbers)
        print("Number of ways: ", count_ways(n, numbers))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
