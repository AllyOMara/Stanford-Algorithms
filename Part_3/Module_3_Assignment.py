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
belong to the maximum-weight independent set (IS)? (By "vertex 1" we mean the
first vertex of the graph---there is no vertex 0.) Output an 8-bit string, where
the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight
independent set, and 0 otherwise.
"""

import sys


def create_node_weights(file_name):
    """ Reads file and returns array containing all node weights
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
    is_weights = []
    for i in range(max_range):
        is_weights.append(None)
    return is_weights


def calculate_is_weight(is_array, weights, max_node):
    """ Recurses on itself to compute the total weight of the optimal IS.
    * Recursively compute max weight IS of G' (one node removed)
    * Recursively compute max weight IS of G'' (two nodes removed) (with first node)
    * Return best max weight IS
    * Maintain array (A) to store solved subprob sizes

    i.e: A[0] = 0, A[1] = w1, for i = 2,3,...,n, A[i] = max{A[i-1], A[i-2] + wi}.
    """

    graph_len = len(weights) - 1
    weight_i = weights[max_node]
    prev_calculated_weight = is_array[max_node]

    if max_node == graph_len - 1:
        optimum_weight = max(weights[graph_len], weights[graph_len - 1])
        is_array[max_node] = optimum_weight
        return optimum_weight

    else:
        for i in range(max_node, graph_len - 1):
            weight_i = weights[max_node]
            if max_node < graph_len - 1:
                is_weight_one = calculate_is_weight(is_array, weights, i + 1) # Recurse on G'
                is_weight_two = calculate_is_weight(is_array, weights, i + 2) + weight_i # Recurse on G''
                best_weight = max(is_weight_one, is_weight_two)
                is_array_index = is_array[max_node]
                if is_array_index != None:
                    if is_array_index < best_weight:
                        is_array[max_node] = best_weight    
                elif is_array_index == None:
                    is_array[max_node] = best_weight


    if prev_calculated_weight == None:
        optimum_weight = 0
        for j in range(max_node, graph_len + 1, 2):
            vertex_weight = weights[j]
            optimum_weight = optimum_weight + vertex_weight
    else:
        optimum_weight = prev_calculated_weight
    return optimum_weight


def reconstruct_is():
    """ Uses the array A from calculate_is_weight to output the max weight IS.
    Scans A from right to left to see which nodes are added to the mas weight IS.
    """

    # Get the filled in array A
    # Set i to the length of A
    # Set the solution (the IS) to an empty list
    # Iterate from right to left (i.e. while i >= 1)
        # If A[i - 1] >= A[i - 2] + wi  (i.e. Case 1 wins)
            # Decrease i by 1
        # Else                          (i.e. Case 2 wins)
            # Add vi to S
            # Decrease i by 1
    # Return S


def output(final_is, output_file):
    """ Check if a set of vertices are within the max weight IS    
    """
    output_array = []
    with open(output_file) as file:
        for line in file:
            vertex = int(line) - 1
            if final_is[vertex] == True:
                output_array.append(1)
            else:
                output_array.append(0)

    # Initialise empty array A
    # Check if the set vertices are in the max weight IS
        # If within max weight IS:
            # Add 1 to an array
        # If not within max weight IS:
            # Add 0 to an array
    # Return A


def max_weight_is():
    """ Calls other functions
    """

    sys.setrecursionlimit(1000000)

    FILE_NAME_1 = "mwis.txt"            # Assigned file, MAX_RANGE = 1000
    FILE_NAME_2 = "mwis_test_1.txt"     # Max sum: 2616, MAX_RANGE = 10
    OUTPUT_FILE_1 = "mwis_vertices.txt" # List of vertices to process in output
    MAX_RANGE = 10
    chosen_file = FILE_NAME_2
    chosen_output = OUTPUT_FILE_1

    weights = create_node_weights(chosen_file)
    is_weights = create_is_weights_list(MAX_RANGE)
    is_weights[MAX_RANGE -1] = weights[MAX_RANGE - 1]
    is_array = calculate_is_weight(is_weights, weights, 0)
    print("hello")


def main():
    max_weight_is()


if __name__ == "__main__":
    main()