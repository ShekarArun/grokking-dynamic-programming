""" 
This program is the naive solution for the Tribonacci Numbers problem

Problem Statement:
Find the 'n'th Tribonacci number.
The Tribonacci sequence is defined as:
F0 = 0, F1 = 1, F2= = 1, F(n) = F(n-1) + F(n-2) + F(n-3) for n>=3

eg:
n = 5
The sequence built using the definition will be 0, 1, 1, 2, 4
So n = 5 => The Tribonacci number is 4

Time Complexity: O(2^n) because for each number we recursively calculate two subproblems (not sure how it isn't 3^n)
Space complexity: O(n) as the maximum depth of the recursive chain is n
"""

from inputs import tests
from time import time  # To calculate runtime


def get_tribonacci(n: int) -> int:
    if n < 2:
        return n
    if n == 2:
        return 1

    return get_tribonacci(n - 1) + get_tribonacci(n - 2) + get_tribonacci(n - 3)


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        n = test["n"]
        print("=" * 30)
        print("n: ", n)
        print("Tribonacci Number: ", get_tribonacci(n))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
