"""
Stanford Algorithms - Part 3 Module 4
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
second item has value 50074 and size 659, respectively.

What is the value of the optimal solution?
"""


def create_item_values(file_name):
    """ Creates and returns array of all item values.
    """


def create_item_weights(file_name):
    """ Creates and returns array of all item weights.
    """


def find_knapsack_size(file_name):
    """ Finds and returns knapsack size.
    """


def find_max_items(file_name):
      """ Finds and returns the maximum number of items.
    """  


def create_knapsack_array(max_items, knapsack_size):
    """ Creates a 2D array of size max_items containing arrays of size knapsack_size.
    - Also initialises A[0][x] = 0 for all x = 0, 1, W
    """


def find_knapsack_value(knapsack_array, item_values, item_weights):
    """ Finds and returns the value of the optimal solution.
    """


def knapsack():
    """ Knapsack dynamic programming algorithm used to find the optimal solution to the knapsack problem.
    """


def main():
    knapsack()


if __name__ == "__main__":
    main()