"""
Test file for Week_1_Assignment.py

Contains _ test cases.

"""


import Week_3_Assignment as week


def test_1():
    answer = week.tsp_heuristic("Test_TSP_1.txt")
    assert answer == 23


def test_2():
    answer = week.tsp_heuristic("Test_TSP_2.txt")
    assert answer == 683


def test_3():
    answer = week.tsp_heuristic("Test_TSP_3.txt")
    assert answer == 93


def test_4():
    answer = week.tsp_heuristic("Test_TSP_4.txt")
    assert answer == 7088245


def test_5():
    answer = week.tsp_heuristic("Test_TSP_5.txt")
    assert answer == 7060869