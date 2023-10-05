""" 
This program is the Bottom-Up (Tabulation) solution for the Unbounded Knapsack problem

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

Note:
- Can optimize space complexity to be O(capacity) by taking a 1D array to store intermediate values, as anyway the same values are required
- Was also thinking about how inner loop can start from the weight of the current item, as until that point the solution would be same as not considering that item, i.e. Existing values in array (Although that doesn't improve worst case time complexity) -> Update, this is indeed what is done, which is why we check if the current item's weight is within capacity.
"""

from inputs import tests
from time import time  # To calculate runtime


def find_knapsack(capacity, weights, values, n):
    dp = [[0 for i in range(capacity + 1)] for j in range(n)]

    # In the first row, all capacities >= the first weight can be calculating by using max quantity of the same (first) item
    for j in range(weights[0], capacity + 1):
        dp[0][j] = (j // weights[0]) * values[0]

    for i in range(1, n):  # First row has been populated, so start from 1
        for j in range(0, capacity + 1):
            # Current i value indicates element number i being taken into consideration
            # Current j value indicates the capacity considered for this problem subset

            # Next, see whether the current weight being considered can be added to the knapsack
            # If it can, that means we have two options -> Either take it or don't
            # So take the max between the two possibilities
            if weights[i] <= j:
                taken = values[i] + dp[i][j - weights[i]]
                not_taken = dp[i - 1][j]
                dp[i][j] = max(taken, not_taken)
            else:
                # The weight exceeds the remaining capacity, so this item cannot be considered -> Same logic as not considering this item
                dp[i][j] = dp[i - 1][j]

    # Finally, the highest value can be obtained by checking the solution for input capacity and input number of items, which will be the bottom right element in the matrix
    return dp[n - 1][-1]


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
