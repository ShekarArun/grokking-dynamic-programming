""" 
This program is the naive solution for the Number of Ways to Score in a Game problem

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
