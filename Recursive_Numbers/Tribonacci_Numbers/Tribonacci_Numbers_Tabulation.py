""" 
This program is the Bottom-Up (Tabulation) solution for the Tribonacci Numbers problem

Problem Statement:
Find the 'n'th Tribonacci number.
The Tribonacci sequence is defined as:
F0 = 0, F1 = 1, F2= = 1, F(n) = F(n-1) + F(n-2) + F(n-3) for n>=3

eg:
n = 5
The sequence built using the definition will be 0, 1, 1, 2, 4
So n = 5 => The Tribonacci number is 4

Time Complexity: O(n) as we go through a loop of n iterations
Space complexity: O(n) as we initialize a dp array of size n
"""

from inputs import tests
from time import time  # To calculate runtime


def get_tribonacci(n: int) -> int:
    if n < 2:
        return n
    if n == 2:
        return 1

    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


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
