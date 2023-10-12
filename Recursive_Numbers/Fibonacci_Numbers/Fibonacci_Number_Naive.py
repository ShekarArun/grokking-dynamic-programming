""" 
This program is the naive solution for the Fibonacci Numbers problem

Problem Statement:
Find the 'n'th Fibonacci number.
The Fibonacci sequence is defined as:
F0 = 0, F1 = 1, F(n) = F(n-1) + F(n-2) for n>=2

eg:
n = 4
The sequence built using the definition will be 0, 1, 1, 2, 3
So n = 4 => The Fibonacci number is 2

Time Complexity: O(2^n) because for each number we recursively calculate two subproblems
Space complexity: O(n) as the maximum depth of the recursive chain is n
"""

from inputs import tests
from time import time  # To calculate runtime


def get_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return get_fibonacci(n - 2) + get_fibonacci(n - 1)


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        n = test["n"]
        print("=" * 30)
        print("n: ", n)
        print("Fibonacci Number: ", get_fibonacci(n))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
