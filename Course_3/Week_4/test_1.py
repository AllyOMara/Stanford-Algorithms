"""
Test file for Week_4_Assignment_Part_1.py

Contains 4 test cases.

"""

import Week_4_Assignment_Part_1 as week


def test_find_knapsack_value():
    
    assert week.find_knapsack_value([[0, 0, 0, 0, 0, 0], [None, None, None, None, None, None,], [None, None, None, None, None, None,],
                                       [None, None, None, None, None, None,]], [0, 1, 2, 3], [0, 3, 2, 1], 5, 3) == 5
    
    assert week.find_knapsack_value([[0, 0, 0, 0], [None, None, None, None, None], [None, None, None, None, None],
                                       [None, None, None, None, None], [None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None]], [0,8,2,7,10,7], [0,2,1,3,2,2], 3, 5) == 12
    
    assert week.find_knapsack_value([[0, 0, 0, 0, 0, 0, 0, 0], [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None]], [0,11,13,12,3,9,10], [0,6,2,3,1,1,2], 7, 6) == 37
    
    assert week.find_knapsack_value([[0, 0, 0, 0, 0, 0, 0, 0, 0], [None, None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None, None]], [0,2,2,2,2,2,2,2,6], [0,1,1,1,1,1,1,1,6], 8, 8) == 14
