"""
Test file for Week_1_Assignment.py

Contains 4 test cases.

"""


import Week_1_Assignment as week


def test_1():
    answer = week.find_shortest_shortest_path("test_graph_1.txt")
    assert answer == -41


def test_2():
    answer = week.find_shortest_shortest_path("test_graph_2.txt")

    assert answer == -208


def test_3():
    answer = week.find_shortest_shortest_path("test_graph_3.txt")
    assert answer == -431


def test_4():
    answer = week.find_shortest_shortest_path("test_graph_4.txt")
    assert answer == "NULL"