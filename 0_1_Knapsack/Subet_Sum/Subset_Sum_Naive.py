""" 
This program is the naive solution for the Subset Sum problem

Problem Statement:
Given an array of positive integers 'arr' and a value 'total', determine if there exists a subset in the given set whose sum adds up to 'total'.

eg:
Consider arr = [1, 2, 3, 7] and T = 6
The subset [1, 2, 3] adds up to 6, so the result is TRUE

Time Complexity: O(2^n), because for each element we have an option to either take it or leave it
Space Complexity: O(n), as the recursive call goes up to a maximum depth of n
"""

from inputs import tests
from time import time  # To calculate runtime


def find_subset_sum(arr, total):
    n = len(arr)
    return find_subset_sum_rec(arr, n, total)


def find_subset_sum_rec(arr, n, total):
    """
    Logic:
    Parse the complete array moving backwards. Recursively call two possible outputs -> Either taking the current element or skipping it.
    If considering any element to contribute to the total, reduce it from the total so we know how much remainin total is to be achieved
    At any point in a recursive chain, if the total is 0, then we have achieved a combination to add up to that value
    """
    # Base condition in case total is achieved
    if total == 0:
        return True

    # If we have run out of elements, then we cannot scope further and the total has not been achieved
    if n == 0:
        return False

    # If the current value is greater than the remaining total, it can directly be skipped
    if arr[n - 1] > total:
        return find_subset_sum_rec(arr, n - 1, total)

    # The two possibilities to proceed are to either consider or skip this value in the array
    return (find_subset_sum_rec(arr, n - 1, total)) or (
        find_subset_sum_rec(arr, n - 1, total - arr[n - 1])
    )


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        arr = test["arr"]
        total = test["total"]
        print("=" * 30)
        print("Array: ", arr)
        print("Total: ", total)
        print("Result: ", find_subset_sum(arr, total))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()
