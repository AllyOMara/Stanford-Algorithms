def create_knapsack_array(max_items, knapsack_size):
    """ Creates a 2D array of size max_items containing arrays of size knapsack_size.
    - Also initialises A[0][x] = 0 for all x = 0, 1, W
    """
    
    knapsack_array = []
    for i in range(max_items):
        knapsack_array.append([])
    for i in range(max_items):
        for j in range(knapsack_size):
            knapsack_array[i].append(None)
    for i in range(knapsack_size):
        knapsack_array[0][i] = 0
    return(knapsack_array)

arr = create_knapsack_array(8, 8)
print(arr)