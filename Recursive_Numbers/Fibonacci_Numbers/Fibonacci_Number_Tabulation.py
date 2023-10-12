""" 
This program is the Bottom-Up (Tabulation) solution for the Fibonacci Numbers problem

Problem Statement:
Find the 'n'th Fibonacci number.
The Fibonacci sequence is defined as:
F0 = 0, F1 = 1, F(n) = F(n-1) + F(n-2) for n>=2

eg:
n = 4
The sequence built using the definition will be 0, 1, 1, 2, 3
So n = 4 => The Fibonacci number is 2

Time Complexity: O(n) as loop through all numbers up to n
Space complexity: O(n) as we initialize a dp of size n
"""

from inputs import tests
from time import time  # To calculate runtime


def get_fibonacci(n: int) -> int:
    if n < 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


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
