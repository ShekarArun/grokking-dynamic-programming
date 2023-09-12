""" 
This program is the naive solution for the 0/1 Knapsack problem

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

Time Complexity: O(2^n) because for each weight we have a subproblem where we either choose or do not choose it
Space complexity: O(n)
"""

from inputs import tests
from time import time  # To calculate runtime


def find_knapsack(capacity, weights, values, n):
    # Base condition to exit from recursive call
    if n == 0 or capacity == 0:
        return 0

    # Check if current weight is lesser than remaining capacity
    if weights[n - 1] <= capacity:
        # This means it is a possible option to be considered for the final solution
        # So take the max between options of either considering this weight or not considering it
        return max(
            (
                values[n - 1]
                + find_knapsack(capacity - weights[n - 1], weights, values, n - 1)
            ),
            find_knapsack(capacity, weights, values, n - 1),
        )
    else:
        # The weight exceeds remaining capacity so cannot be considered
        return find_knapsack(capacity, weights, values, n - 1)


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
