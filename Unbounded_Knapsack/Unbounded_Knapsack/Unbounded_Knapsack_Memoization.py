""" 
This program is the Top-Down (Memoization) solution for the Unbounded Knapsack problem

Problem Statement:
Suppose you have a list of weights and corresponding values for 'n' items. You have a knapsack that can carry items up to a specific maximum weight, known as the capacity of the knapsack.
You want to maximize the sum of values of the items in your knapsack while ensuring that the sum of weights of those items does not exceed the maximum carrying capacity of the knapsack.
Items can be repeated. There is not limit to the quantity of each item.

If all combinations exceed the given knapsack's capacity, return 0.

eg:
capacity = 10
weights = [2, 4, 6]
values = [5, 11, 13]
The maximum value is obtained by taking the weights [2, 4, 4], which gives a total weight of 27.

Time Complexity: O(n * capacity)
Space complexity: O(n * capacity)
"""

from inputs import tests
from time import time  # To calculate runtime


def find_knapsack(capacity, weights, values, n):
    dp = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]
    return find_knapsack_value(
        capacity, weights, values, n - 1, dp
    )  # Passing (n-1) to adjust for 0 index


def find_knapsack_value(capacity, weights, values, n, dp):
    # If we've reached the last element, fill up the remaining capacity with as much quantity of it as possible
    if n == 0:
        return (capacity // weights[0]) * values[0]

    # Check if the given subproblem already has a solution
    if dp[n][capacity] != -1:
        return dp[n][capacity]

    # Check if current weight is lesser than remaining capacity
    if weights[n] <= capacity:
        # This means it is a possible option to be considered for the final solution
        # So take the max between options of either considering this weight or not considering it
        taken = values[n] + find_knapsack_value(
            capacity - weights[n], weights, values, n, dp
        )
        not_taken = find_knapsack_value(capacity, weights, values, n - 1, dp)
        dp[n][capacity] = max(taken, not_taken)
    else:
        # The weight exceeds remaining capacity so cannot be considered
        dp[n][capacity] = find_knapsack_value(capacity, weights, values, n - 1, dp)

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
