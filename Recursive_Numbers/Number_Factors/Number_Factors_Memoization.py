""" 
This program is the Top-Down (Memoization) solution for the Number Factors problem

Problem Statement:
Given a list of factors and a number 'n', find the number of ways in which the number can be made up as a sum of the factors.
Order matters.

eg:
n = 4
numbers = [1, 3, 4]
The different ways to obtain the given value are:
1. 1 + 1 + 1 + 1
2. 1 + 3
3. 3 + 1
4. 4
So the expected result is '4'.

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
