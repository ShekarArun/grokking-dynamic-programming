""" 
This program is the naive solution for the Number Factors problem

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

Time Complexity: O(2^n) because for each number we recursively pick or don't pick it.
Space complexity: O(n) as the maximum depth of the recursive chain is n
"""

from inputs import tests
from time import time  # To calculate runtime


def count_ways(n: int, numbers: list[int]) -> int:
    if n < 0:
        return 0

    if n == 0:
        return 1

    res = 0

    for number in numbers:
        res += count_ways((n - number), numbers)

    return res


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
