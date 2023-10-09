# These are the test inputs for the Maximum Ribbon Cut problem

test1 = {"length": 4, "sizes": [1, 2, 3, 4], "prices": [2, 3, 7, 8]}
test2 = {"length": 6, "sizes": [1, 2, 3, 4, 5, 6], "prices": [2, 5, 8, 9, 10, 11]}
test3 = {"length": 5, "sizes": [1, 2, 3, 4, 5], "prices": [2, 6, 7, 10, 13]}
test4 = {"length": 3, "sizes": [1, 2, 3], "prices": [3, 7, 8]}
test5 = {"length": 5, "sizes": [3, 2, 1, 4, 5], "prices": [8, 7, 3, 2, 20]}
test6 = {"length": 3, "sizes": [2, 3, 4], "prices": [2, 7, 8]}
test7 = {"length": 6, "sizes": [6, 5, 4, 3, 2, 1], "prices": [2, 8, 9, 10, 11, 1]}
test8 = {"length": 3, "sizes": [1, 2, 3], "prices": [7, 3, 8]}
test9 = {"length": 4, "sizes": [2, 3, 4], "prices": [2, 7, 8]}
test10 = {"length": 8, "sizes": [2, 1], "prices": [20, 10]}
test11 = {"length": 4, "sizes": [4, 3, 2, 1], "prices": [1, 1, 1, 6]}
test12 = {"length": 6, "sizes": [1, 2, 5, 4, 6], "prices": [2, 8, 9, 10, 11]}
test13 = {
    "length": 25,
    "sizes": [17, 9, 15, 20, 5, 21, 8, 1, 24, 14, 12, 4, 18, 11, 10],
    "prices": [43, 63, 56, 53, 65, 52, 58, 87, 37, 91, 56, 78, 80, 52, 44],
}
test14 = {
    "length": 100,
    "sizes": [i for i in range(1, 200, 2)],
    "prices": [i for i in range(1, 101)],
}

tests = [
    test1,
    test2,
    test3,
    test4,
    test5,
    test6,
    test7,
    test8,
    test9,
    test10,
    test11,
    test12,
    test13,
    test14,
]
