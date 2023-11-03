""" 
This program is the Bottom-Up (Tabulation) solution for the House Thief problem

Problem Statement:
A professional robber attempts to rob a street of houses. There is a restriction that adjacent houses cannot be robbed due to security measures.
Given a list of values where each item indicates the value obtained from robbing that particular house, find the maximum value that can be obtained on one night of robbing.

eg:
money = [1, 2, 3, 4, 5]
The possible combinations of houses that can be robbed are:
1. 1 + 3 + 5 = 9
2. 1 + 4 = 5
3. 1 + 5 = 6
4. 2 + 4 = 6
5. 2 + 5 = 7
6. 3 + 5 = 8
7. 4
8. 5

Time Complexity: O(n) as each house has a solution calculated once
Space complexity: O(n) as we utilize a memo of size n
"""

from inputs import tests
from time import time  # To calculate runtime


def house_thief(money: list[int]) -> int:
    size = len(money)

    if size == 0:
        return 0

    dp = [0] * (size + 1)
    dp[1] = money[0]

    for i in range(1, size):
        # money[i] because money is 0-indexed but our calculations on the DP are 1-indexed
        dp[i + 1] = max(dp[i], (money[i] + dp[i - 1]))

    return dp[size]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        money = test["money"]
        print("=" * 30)
        print("Money: ", money)
        print("Max value: ", house_thief(money))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
