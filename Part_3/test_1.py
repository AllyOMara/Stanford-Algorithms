import Module_4_Assignment_Part_1 as module

def test_find_knapsack_value():
    
    assert module.find_knapsack_value([[0, 0, 0, 0, 0], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]],
                                [1, 2, 3], [3, 2, 1], 5, 3) == 5
    
    assert module.find_knapsack_value([[0, 0, 0], [None, None, None], [None, None, None], [None, None, None],
                                [None, None, None, None, None]], [None, None, None, None, None],
                               [8,2,7,10,7], [2,1,3,2,2], 3, 5) == 12
    
    assert module.find_knapsack_value([[0, 0, 0, 0, 0, 0, 0], [None, None, None, None, None, None, None], [None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None], [None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None], [None, None, None, None, None, None, None]],
                                [11,13,12,3,9,10], [6,2,3,1,1,2], 7, 6) == 37
    
    assert module.find_knapsack_value([[0, 0, 0, 0, 0, 0, 0, 0], [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None]], [2,2,2,2,2,2,2,6], [1,1,1,1,1,1,1,6], 8, 8) == 14
    
    # assert find_knapsack_value(knapsack_array, item_values, item_weights, knapsack_size, max_items)