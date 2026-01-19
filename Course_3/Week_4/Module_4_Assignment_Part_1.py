"""
Stanford Algorithms - Course 3 Module 4
Programming Assignment

Solution by Alexandria O'Mara

TASK

This file (knapsack1.txt) describes a knapsack instance.
It has the following format:
[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]
...
For example, the third line of the file is "50074 659", indicating that the
second item has value 50074 and size 659.

What is the value of the optimal solution?
"""


def create_item_values(file_name):
    """ Creates and returns array of all item values.
    Arguments:
        file_name: (String) Inputted file.
    Returns:
        (Array) All item values, where item 1's value is at index 1.
    """

    values = [0]  # Better indexing
    first_line = True
    with open(file_name) as file:
        for line in file:
            if first_line:
                first_line = False
            else:
                item_description = line.split()
                item_value = int(item_description[0])
                values.append(item_value)
    return values


def create_item_weights(file_name):
    """ Creates and returns array of all item weights.
    Arguments:
        file_name: (String) Inputted file.
    Returns:
        (Array) All item weights, where item 1's weight is at index 1.
    """

    weights = [0]  # Better indexing
    first_line = True
    with open(file_name) as file:
        for line in file:
            if first_line:
                first_line = False
            else:
                item_description = line.split()
                item_weight = int(item_description[1])
                weights.append(item_weight)
    return weights


def find_knapsack_size(file_name):
    """ Finds and returns knapsack size.
    Arguments:
        file_name: (String) Inputted file.
    Returns:
        (Integer) Size of the knapsack.
    """

    first_line = True
    with open(file_name) as file:
        for line in file:
            if first_line:
                knapsack_description = line.split()
                knapsack_size = int(knapsack_description[0])
                first_line = False
    return knapsack_size


def find_max_items(file_name):
    """ Finds and returns the maximum number of items.
    Arguments:
        file_name: (String) Inputted file.
    Returns:
        (Integer) Number of items.
    """

    first_line = True
    with open(file_name) as file:
        for line in file:
            if first_line:
                knapsack_description = line.split()
                max_items = int(knapsack_description[1])
                first_line = False
    return max_items


def create_knapsack_array(max_items, knapsack_size):
    """ Creates a 2D array of size max_items containing arrays of size knapsack_size.
    Arguments:
        max_items: (Integer) total number of items.
        knapsack_size: (Integer) total size of knapsack.
    Returns:
        (Array) 2D array size max_items * knapsack_size.
    """

    knapsack_array = []
    for i in range(max_items + 1):
        knapsack_array.append([])
    for i in range(max_items + 1):  # Fixes indexing
        for j in range(knapsack_size + 1):  # Fixes indexing
            knapsack_array[i].append(None)
    for i in range(knapsack_size + 1):  # Initialise A[0][x] = 0 for all x = 0, 1, W
        knapsack_array[0][i] = 0
    return knapsack_array


def find_knapsack_value(knapsack_array, item_values, item_weights, knapsack_size, max_items):
    """ Finds and returns the value of the optimal solution.
    Arguments:
        knapsack_array: (Array) stores total values of items in the knapsack.
        item_values: (Array) All item values.
        item_weights: (Array) All item weights.
        knapsack_size: (Integer) Knapsack weight limit.
        max_items: (Integer) Total number of items.
    Returns:
        Optimum total value of items in the knapsack.
    """

    for i in range(1, max_items + 1):
        weight_i = item_weights[i]
        value_i = item_values[i]
        for x in range(0, knapsack_size + 1):
            case_1 = knapsack_array[i - 1][x]
            if weight_i > x:
                case_2 = 0  # Ignores item
            else:
                case_2 = knapsack_array[i - 1][x - weight_i] + value_i
            knapsack_array[i][x] = max(case_1, case_2)
    return knapsack_array[max_items][knapsack_size]


def knapsack():
    """ Knapsack algorithm used to find the optimal solution.
    """

    FILE = "knapsack1.txt"  # Assigned file
    
    values = create_item_values(FILE)
    weights = create_item_weights(FILE)
    knapsack_size = find_knapsack_size(FILE)
    max_items = find_max_items(FILE)
    knapsack_array = create_knapsack_array(max_items, knapsack_size)
    knapsack_value = find_knapsack_value(knapsack_array, values, weights, knapsack_size, max_items)

    print(knapsack_value)


def main():
    knapsack()


if __name__ == "__main__":
    main()