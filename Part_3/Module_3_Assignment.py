"""
Stanford Algorithms - Part 3 Module 3
Programming Assignment

Solution by Alexandria O'Mara

TASK

This file describes the weights of the vertices in a path graph (with the
weights listed in the order in which vertices appear in the path).
It has the following format:
[number_of_vertices]
[weight of first vertex]
[weight of second vertex]
...
For example, the third line of the file is "6395702," indicating that the weight
of the second vertex of the graph is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and the
reconstruction procedure) from lecture on this data set.

The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones
belong to the maximum-weight independent set (IS)? Output an 8-bit string, where
the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight
independent set, and 0 otherwise.
"""

import sys


def create_node_weights(file_name):
    """ Reads file and returns array containing all node weights.
    Arguments:
        file_name: (String) Inputted file to create list of node weights.
    Returns:
        (Array) All node weights in an array.
    """

    weights = []
    first_line = True
    with open(file_name) as file:
        for line in file:
            if first_line:
                first_line = False
            else:
                weights.append(int(line))
    return weights
            

def create_is_weights_list(max_range):
    """ Create and return an empty list of length max_range.
    Arguments:
        max_range: (Integer) highest node number.
    Returns:
        (Array) Empty array size max_range.
    """

    is_weights = []
    for i in range(max_range):
        is_weights.append(None)
    return is_weights


def calculate_is_weight(is_array, weights, max_node):
    """ Calculate and return the total weight of the optimal IS. \n
    
    Uses recursion to compute the total weight of the optimal IS. Through using
    an optimised brute force algorithm (i.e. using dynamic programming, through
    employment of an array to store previously computed values to remove
    redundant calculations), calculates the optimal IS of smaller subproblems
    to calculate the optimal IS of the overall problem. Processes is_array to
    compute weights of optimal subproblems to be used in reconstructing the IS.

    Arguments:
        is_array: (Array) Optimal IS sizes (to improve run time).
        weights: (Array) All node weights.
        max_node: (Integer) Represents maximum node value from which recursion occurs.
    
    Returns:
        (Integer) Optimum weight.
    """

    graph_len = len(weights) - 1
    prev_calculated_weight = is_array[max_node]

    if prev_calculated_weight != None:  # Already computed total weight
        return prev_calculated_weight

    if max_node == graph_len - 1:  # Two nodes
        optimum_weight = max(weights[graph_len], weights[graph_len - 1])
        is_array[max_node] = optimum_weight
        return optimum_weight

    else:
        for i in range(max_node, graph_len - 1):
            weight_i = weights[max_node]

            if max_node < graph_len - 1:
                is_weight_one = calculate_is_weight(is_array, weights, i + 1)  # Recurse on G'
                is_weight_two = calculate_is_weight(is_array, weights, i + 2) + weight_i  # Recurse on G''
                best_weight = max(is_weight_one, is_weight_two)
                previously_calculated_weight = is_array[max_node]

                if previously_calculated_weight != None:
                    if previously_calculated_weight < best_weight:
                        is_array[max_node] = best_weight   

                else:
                    is_array[max_node] = best_weight

    if prev_calculated_weight == None:
        optimum_weight = 0
        for j in range(max_node, graph_len + 1, 2):
            vertex_weight = weights[j]
            optimum_weight = optimum_weight + vertex_weight
    else:
        optimum_weight = prev_calculated_weight

    return optimum_weight


def reconstruct_is(is_array, weights):
    """ Uses the array A from calculate_is_weight to output the max weight IS.
    Scans A from right to left to see which nodes are added to the mas weight IS.
    """

    len_weights = len(weights)
    i = len(weights)
    is_array.append(0)
    is_array.reverse()
    weights.append(0)
    weights.reverse()
    solution = []
    while i >= 1:   
        if is_array[i - 1] >= (is_array[i - 2] + weights[i]):  # i.e. Case 1 wins
            i = i - 1
        else:  # i.e. Case 2 wins
            solution.append(len_weights - i + 1)
            i = i - 2
    return solution


def output(final_is, output_file):
    """ Check if a set of vertices are within the max weight IS    
    """
    output_array = []
    with open(output_file) as file:
        for line in file:
            vertex = int(line)
            if vertex in final_is:
                output_array.append(1)
            else:
                output_array.append(0)
    return output_array


def max_weight_is():
    """ Calls other functions
    """

    sys.setrecursionlimit(1000000)

    FILE_NAME_1 = "mwis.txt"            # Assigned file, MAX_RANGE = 1000
    FILE_NAME_2 = "mwis_test_1.txt"     # Max sum = 2617, MAX_RANGE = 10
    FILE_NAME_3 = "mwis_test_2.txt"     # Max sum = 2533, MAX_RANGE = 10
    OUTPUT_FILE_1 = "mwis_vertices.txt" # List of vertices to process in output
    OUTPUT_FILE_2 = "mwis_test_1_vertices.txt"  # Expected output = 0101001001
    OUTPUT_FILE_3 = "mwis_test_2_vertices.txt"  # Expected output = 1010010010
    MAX_RANGE = 1000
    chosen_file = FILE_NAME_1
    chosen_output = OUTPUT_FILE_1

    weights = create_node_weights(chosen_file)
    is_array = create_is_weights_list(MAX_RANGE)
    is_array[MAX_RANGE -1] = weights[MAX_RANGE - 1]
    calculate_is_weight(is_array, weights, 0)
    solution_set = reconstruct_is(is_array, weights)
    solution_array = output(solution_set, chosen_output)
    print(solution_array)


def main():
    max_weight_is()


if __name__ == "__main__":
    main()