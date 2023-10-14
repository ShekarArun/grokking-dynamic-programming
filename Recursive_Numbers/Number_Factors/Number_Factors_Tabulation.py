""" 
This program is the Bottom-Up (Tabulation) solution for the Number Factors problem

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


def count_ways(n: int, numbers: list[int]) -> int:
    dp = [0] * (n + 1)

    dp[0] = 1

    for i in range(n + 1):
        for number in numbers:
            if i - number >= 0:
                dp[i] += dp[i - number]

    return dp[n]


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
