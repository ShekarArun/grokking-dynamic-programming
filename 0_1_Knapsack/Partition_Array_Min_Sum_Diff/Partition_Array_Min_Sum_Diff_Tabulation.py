""" 
This program is the Bottom-Up (Tabulation) solution for the Partition Array for Min Sum Difference problem

Problem Statement:
Given an array of positive integers 'arr', partition the array into two arrays such that the absolute difference between their sums is minimized.

eg:
Consider arr = [1, 2, 3]
The array can be partitioned into [1, 2] and [3], such that the sums of the two arrays are 3 and 3. So, the absolute difference is 3 - 3 = 0

Time Complexity: O(n * (S/2 + 1)), where S is the sum of all elements in the input array
Space Complexity: O(n * (S/2 + 1)), where S is the sum of all elements in the input array

Note:
- Can reduce space complexity by keeping only two rows, the previous and current. (then space complexity becomes O(S/2 + 1))
"""

from inputs import tests
from time import time  # To calculate runtime


def min_partition_arr_sum_diff(arr):
    """
    Logic:
    Build a DP array where the rows indicate the elements in the array and columns indicate the sum of array elements.
    Note: When splitting an array, our intention is for the sum of partitions to tend to the midpoint of the total array sum (i.e. S/2). So we can build our DP array with columns up to S/2, and the remaining value would be in the other partition.

    The value of a cell is intended to be 1 if the corresponding sum (column index) can be obtained by either taking/leaving the array element. If not, the cell value is set to 0.
    Once the DP array is built, we traverse the last row in reverse to find the highest 'sum' that can be generated with the array elements. The remaining from the total is the second sum, and the absolute difference between the two is to be returned.
    """
    # Obtain number of rows and columns
    total = sum(arr)
    rows = len(arr)
    cols = (total // 2) + 1

    # Initialize DP array
    dp = [[-1 for _ in range(cols)] for _ in range(rows)]

    # Note: It helps to think of the DP as representing only the first partition, so the second partition will be the complement of the first.

    # The first column indicates a sum of 0 for the partition, which can always by achieved by making the partition as an empty array
    for i in range(rows):
        dp[i][0] = 1

    # The first row corresponds to selecting the first array element. So the only '1' in this would be the column equal to the array element itself
    for j in range(1, cols):  # Skip first column as that is achievable with empty set
        dp[0][j] = 1 if j == arr[0] else 0

    # Now, iterate and fill the DP array as per the defined logic
    for i in range(1, rows):
        for j in range(1, cols):
            # If the previous row has achieved the sum, then this row can also achieve it without taking the current array element
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]

            # Otherwise, see if the current sum can be obtained by including the current array element
            elif j >= arr[i]:
                dp[i][j] = dp[i - 1][j - arr[i]]

            # Now if neither condition is satisfied, that implies the current array element cannot contribute to the current sum (column)
            # So, set the value to 0, as sum cannot be achieved
            else:
                dp[i][j] = 0

    # Now, we have built our DP array. We need to find the value closest to the mid of the total array sum
    for j in range(cols - 1, -1, -1):
        if dp[-1][j]:
            sum1 = j
            sum2 = total - sum1
            return abs(sum1 - sum2)


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        arr = test["arr"]
        print("=" * 30)
        print("Array: ", arr)
        print("Result: ", min_partition_arr_sum_diff(arr))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
