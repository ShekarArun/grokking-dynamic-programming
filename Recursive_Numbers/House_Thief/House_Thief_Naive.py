""" 
This program is the naive solution for the House Thief problem

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

Time Complexity: O(2^n) because for each number we recursively calculate two subproblems
Space complexity: O(n) as the maximum depth of the recursive chain is n, and each call stores its data on the call stack
"""

from inputs import tests
from time import time  # To calculate runtime


def house_thief(money: list[int], ix: int) -> int:
    size = len(money)

    if ix >= size:
        return 0

    new_ix = ix + 1

    return max(house_thief(money, new_ix), (money[ix] + house_thief(money, new_ix + 1)))


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        money = test["money"]
        print("=" * 30)
        print("Money: ", money)
        print("Max value: ", house_thief(money, 0))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
