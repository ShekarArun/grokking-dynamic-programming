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

Note:
- Can optimize space complexity to be O(capacity) by taking a 1D array to store intermediate values, as anyway the same values are required
- Was also thinking about how inner loop can start from the weight of the current item, as until that point the solution would be same as not considering that item, i.e. Existing values in array (Although that doesn't improve worst case time complexity)
"""

from inputs import tests
from time import time  # To calculate runtime


def find_knapsack(capacity, weights, values, n):
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            # Current i value indicates the number of elements taken into consideration to solve the problem
            # Current j value indicates the capacity considered for this problem subset

            # So of course, either considering 0 items or 0 capacity does not allow us to pick up any item, so set those values to 0
            if i == 0 or j == 0:
                dp[i][j] == 0
            # Next, see whether the current weight being considered can be added to the knapsack
            # If it can, that means we have two options -> Either take it or don't
            # So take the max between the two possibilities
            elif (
                weights[i - 1] <= j
            ):  # Note, i follows the number of elements taken into consideration and j follows the capacity
                dp[i][j] = max(
                    (
                        values[i - 1] + dp[i - 1][j - weights[i - 1]]
                    ),  # Here, we select the current element and add the previously calculated max for remaining capacity (n remains same, hence passing i - 1)
                    dp[i - 1][
                        j
                    ],  # If we don't select it, find the max value for same n elements, but with no reduction in capacity
                )
            else:
                # The weight exceeds the remaining capacity, so this item cannot be considered -> Same logic as not considering this item
                dp[i][j] = dp[i - 1][j]

    # Finally, the highest value can be obtained by checking the solution for input capacity and input number of items, which will be the bottom right element in the matrix
    return dp[-1][-1]


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
