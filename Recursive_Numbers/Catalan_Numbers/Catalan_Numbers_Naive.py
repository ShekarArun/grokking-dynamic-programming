""" 
This program is the naive solution for the Catalan Numbers problem

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

Time Complexity: O(3^n) as we loop over n and for each value ranging up to n, we calculate two recursive solutions
Space complexity: O(n) as the maximum depth of the recursive chain is n
"""

from inputs import tests
from time import time  # To calculate runtime


def get_catalan(n: int) -> int:
    if n == 0:
        return 1

    sum = 0
    for i in range(n):
        sum += get_catalan(i) * get_catalan(n - 1 - i)

    return sum


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
