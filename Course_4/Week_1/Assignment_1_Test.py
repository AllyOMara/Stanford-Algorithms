"""
Test file for Week_1_Assignment.py

Contains 4 test cases.

"""


import Week_1_Assignment as week


def test_1():
    file_name = "test_graph_1.txt"
    answer = week.find_shortest_shortest_path(file_name)
    assert answer == -41


def test_2():
    file_name = "test_graph_2.txt"
    answer = week.find_shortest_shortest_path(file_name)

    assert answer == -208


def test_3():
    file_name = "test_graph_3.txt"
    answer = week.find_shortest_shortest_path(file_name)
    assert answer == -431


def test_4():
    file_name = "test_graph_4.txt"
    answer = week.find_shortest_shortest_path(file_name)
    assert answer == "NULL"