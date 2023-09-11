""" 
This program is the Bottom-Up (Tabulation) solution for the 0/1 Knapsack problem

Problem Statement:
Suppose you have a list of weights and corresponding values for 'n' items. You have a knapsack that can carry items up to a specific maximum weight, known as the capacity of the knapsack.
You want to maximize the sum of values of the items in your knapsack while ensuring that the sum of weights of those items does not exceed the maximum carrying capacity of the knapsack.

If all combinations exceed the given knapsack's capacity, return 0.

eg:
capacity = 5
weights = [1, 2, 3, 5]
values = [10, 5, 4, 8]
In this case, there are 4 ways to store items in the knapsack within the maximum capacity:
1. weights: [1, 2]; total_value = 15
2. weights: [1, 3]; total_value = 14
3. weights: [2, 3]; total_value = 9
4. weights: [5]; total_value = 8

Time Complexity: O(n * capacity)
Space complexity: O(n * capacity)
"""

from inputs import tests
from time import time  # To calculate runtime


def find_knapsack(capacity, weights, values, n):
    dp = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]
    return find_knapsack_value(capacity, weights, values, n, dp)


def find_knapsack_value(capacity, weights, values, n, dp):
    # print("capacity", capacity, "n", n)
    # Base condition to exit from recursive call
    if n == 0 or capacity == 0:
        # print("dp", dp)
        return 0

    # Check if the given subproblem already has a solution
    if dp[n][capacity] != -1:
        # print("dp", dp)
        return dp[n][capacity]

    # Check if current weight is lesser than remaining capacity
    if weights[n - 1] <= capacity:
        # This means it is a possible option to be considered for the final solution
        # So take the max between options of either considering this weight or not considering it
        dp[n][capacity] = max(
            (
                values[n - 1]
                + find_knapsack_value(
                    capacity - weights[n - 1], weights, values, n - 1, dp
                )
            ),
            find_knapsack_value(capacity, weights, values, n - 1, dp),
        )
    else:
        # The weight exceeds remaining capacity so cannot be considered
        dp[n][capacity] = find_knapsack_value(capacity, weights, values, n - 1, dp)
    # print("dp", dp)
    return dp[n][capacity]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        weights = test["weights"]
        values = test["values"]
        capacity = test["capacity"]
        print("=" * 30)
        print("Weights: ", weights)
        print("Values: ", values)
        print("Capacity: ", capacity)
        print("Max Value: ", find_knapsack(capacity, weights, values, len(weights)))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
