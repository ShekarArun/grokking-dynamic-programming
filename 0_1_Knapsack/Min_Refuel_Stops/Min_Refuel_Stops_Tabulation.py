""" 
This program is the Bottom-Up (Tabulation) solution for the Minimum Number of Refuel Stops problem

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
    """
    Logic:
    DP Matrix represents the distance that can be covered taking r stations into consideration and with c stops
    Loop through matrix, storing max distance for each combination of r and c
    Finally, find the lowest c value required in the last row (considering all stations) to reach the target
    """
    # Base condition: If no stations, directly return based on initial fuel
    if start_fuel >= target:
        return 0

    n = len(stations)

    # Initialize DP Array to store the maximum distance from index i with j stops
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # With no stops, the max distance is always same as start fuel, so set column 0 to start fuel value
    for i in range(n + 1):
        dp[i][0] = start_fuel

    # Now, find the max distance for each combination of stations and stops
    for i in range(1, n + 1):
        # Loop through columns from 1 stop to i number of stops, where i represents number of stations considered -> Can't make more stops than that anyway
        for j in range(1, i + 1):
            # Check if excluding this station, the max distance we could cover allows us to reach this station
            if dp[i - 1][j - 1] >= stations[i - 1][0]:
                # Since we can reach this station, the new max can be obtained either by skipping this station
                skip_stop = dp[i - 1][j]
                # Or by refueling at this stop
                take_stop = dp[i - 1][j - 1] + stations[i - 1][1]
                dp[i][j] = max(skip_stop, take_stop)
            else:
                # Otherwise, we can't reach this station anyway, so the max distance will be the same as what we could achieve while excluding this station
                dp[i][j] = dp[i - 1][j]

    # Now, we know the maximum distance we can cover with each number of stops
    # So, proceed to find the lowest index which can cover the target distance (which implies minimum number of stops)
    for i in range(n + 1):
        if dp[n][i] >= target:
            return i

    # If we haven't reached target in any of the number of stops, return -1 as the target cannot be reached
    return -1


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
