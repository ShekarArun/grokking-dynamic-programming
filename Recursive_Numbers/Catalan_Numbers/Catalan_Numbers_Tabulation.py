""" 
This program is the Bottom-Up (Tabulation) solution for the Catalan Numbers problem

Problem Statement:
Find the 'n'th Catalan number.
The Catalan sequence is defined as:
C(0) = 1
C(n) = sum(C(i) * C(n - 1 - i)) for i in [0, n-1]

eg:
n = 4
C(4) = C(0)*C(3) + C(1)*C(2) + C(2)*C(1) + C(3)*C(0)
C(4) = 1*5 + 1*2 + 2*1 + 5*1
C(4) = 14
The sequence built using the definition will be 1, 1, 2, 5, 14, 42, 132, ...
So n = 4 => The Catalan number is 14

Time Complexity: O(n^2) as each Catalan number is calculated by precomputed results of the previous Catalan Numbers
Space complexity: O(n) as the DP array is of size n
"""

from inputs import tests
from time import time  # To calculate runtime


def get_catalan(n: int) -> int:
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    # Initial condition
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]

    return dp[n]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        n = test["n"]
        print("=" * 30)
        print("n: ", n)
        print("Catalan Number: ", get_catalan(n))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
