""" 
This program is the Top-Down (Memoization) solution for the Minimum Number of Refuel Stops problem

Problem Statement:
Given:
1. A car with an initial quantity of fuel
2. A target distance
3. A list of fuel stations, represented by their distance from start and the quantity of fuel available there [[distance1, qty1], [distance2, qty2]...]
Determine the minimum number of stops to reach the target distance, assuming the car consumes 1 unit of fuel per unit of distance

If it is not possible to reach the target, return 0

eg:
target = 15
start fuel = 2
stations = [[1, 2], [2, 8], [4, 10], [6, 7], [7, 2], [8, 1]]
The answer is 2 stops ([2, 8] and [4, 10])

Time Complexity: O(n^2)
Space complexity: O(n^2)
"""

# from math import inf
from inputs import tests
from time import time  # To calculate runtime


def min_refuel_stops(target, start_fuel, stations):
    # Base condition: If no stations, directly return based on initial fuel
    if start_fuel == target:
        return 0

    n = len(stations)
    i = 0

    # Initialize DP Array to store the maximum distance from index i with j stops
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    # Store the maximum distance that can be travelled for each number of stops in an array
    max_dist = [-1] * (n + 1)

    # Now, store the maximum distance that can be covered for each number of stops
    for i in range(n + 1):
        max_dist[i] = min_refuel_stops_helper(n, i, start_fuel, stations, dp)

    # Now, we know the maximum distance we can cover with each number of stops
    # So, proceed to find the lowest index which can cover the target distance (which implies minimum number of stops)
    for i in range(n + 1):
        if dp[n][i] >= target:
            return i

    # If we haven't reached target in any of the number of stops, return -1 as the target cannot be reached
    return -1


def min_refuel_stops_helper(index, used, cur_fuel, stations, dp):
    """
    Logic:
    This helper function identifies the maximum distance that can be covered from starting station of 'index', while utilizing 'used' number of stops more
    """
    # If there are no remaining stops that can be made, return the remaining fuel as the maximum distance that can be covered
    if used == 0:
        dp[index][used] = cur_fuel
        return dp[index][used]

    # If there are more stops than number of stations remaining, then we cannot reach the target distance
    if used > index:
        # -2 so that we don't recalculate actual -1 cases (Differentiate between untouched cell and calculated cell but no solution)
        dp[index][used] = -2
        return dp[index][used]

    # If the solution has already been found, return that
    if dp[index][used] != -1:
        return dp[index][used]

    # Now, we can either take or skip the current station
    skip_stop = min_refuel_stops_helper(index - 1, used, cur_fuel, stations, dp)
    take_stop = min_refuel_stops_helper(index - 1, used - 1, cur_fuel, stations, dp)

    # Return the higher between the two distances
    # BUT, if the remaining fuel does not allow us to reach the next station, return -1
    dp[index][used] = max(
        skip_stop,
        -2
        if take_stop
        < stations[index - 1][
            0
        ]  # -2 because we can't reach the next stop with the remaining fuel
        else take_stop
        + stations[index - 1][
            1
        ],  # Add last stop's fuel to the total distance that can be reached, assuming we can travel until this
    )
    return dp[index][used]


def main():
    for test in tests:
        # start_time = datetime.now()
        start_time = time()
        target = test["target"]
        start_fuel = test["start_fuel"]
        stations = test["stations"]
        print("=" * 30)
        print("Target: ", target)
        print("Start Fuel: ", start_fuel)
        print("Stations: ", stations)
        print("Min Stops: ", min_refuel_stops(target, start_fuel, stations))
        print("Total runtime: ", ((time() - start_time) * 10**3), "ms")
        print("=" * 30)


if __name__ == "__main__":
    main()

""" NOTE: Below logic didn't work, off by few counts in various problem statements, so scrapping it """
# def min_refuel_stops(target, start_fuel, stations):
#     return min_refuel_stops_rec(target, start_fuel, stations, 0, 0)


# def min_refuel_stops_rec(target, fuel, stations, pos, stops):
#     """
#     Logic:
#     Starting from the initial position, we can proceed to check each station along the way
#     If we reach the next station, we can choose to either fuel up or skip it (0/1 similarity here)
#     If our remaining fuel is lesser than the specified station, we cannot reach it so return 0
#     Note: Remember to reduce the fuel consumed when traveling from one station to the next
#     """
#     if pos == len(stations):
#         return -1

#     cur_stop = stations[pos]
#     prv_stop = stations[pos - 1] if pos > 0 else None
#     # Find remaining distance
#     rem_dist = target - cur_stop[0]
#     rem_fuel = fuel - (cur_stop[0] - (prv_stop[0] if prv_stop else 0))

#     if rem_dist <= 0:
#         return stops

#     # If we can cover the remaining distance with the given fuel, then return
#     if rem_dist <= fuel:
#         return stops

#     # See if we can reach this stop
#     if rem_fuel < 0:
#         return -1

#     # Else, either consider or skip this stop
#     take_stop = min_refuel_stops_rec(
#         target, rem_fuel + cur_stop[1], stations, pos + 1, stops + 1
#     )
#     skip_stop = min_refuel_stops_rec(target, rem_fuel, stations, pos + 1, stops)

#     if take_stop == -1:
#         return skip_stop
#     elif skip_stop == -1:
#         return take_stop
#     else:
#         return min(take_stop, skip_stop)
