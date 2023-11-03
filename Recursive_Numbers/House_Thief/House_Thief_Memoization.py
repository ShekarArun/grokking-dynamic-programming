""" 
This program is the Top-Down (Memoization) solution for the House Thief problem

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
    dp = [0] * size

    return house_thief_rec(money, 0, size, dp)


def house_thief_rec(money: list[int], ix: int, size: int, dp: list[int]) -> int:
    size = len(money)

    if ix >= size:
        return 0

    if dp[ix] == 0:
        new_ix = ix + 1
        dp[ix] = max(
            house_thief_rec(money, new_ix, size, dp),
            (money[ix] + house_thief_rec(money, new_ix + 1, size, dp)),
        )

    return dp[ix]


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
