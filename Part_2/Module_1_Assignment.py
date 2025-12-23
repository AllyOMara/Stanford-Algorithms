'''
Stanford Algorithms - Part 2 Module 1
Programming Assignment

Solution by Alexandria O'Mara

TASK

This file (SCC.txt) contains the edges of a directed graph.
Vertices are labeled as positive integers from 1 to 875714.
Every row indicates an edge, the vertex label in first
column is the tail and the vertex label in second column is
the head.

Your task is to code up the algorithm from the video
lectures for computing strongly connected components (SCCs),
and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest
SCCs in the given graph, in decreasing order of sizes,
separated by commas (avoid any spaces). If your algorithm
finds less than 5 SCCs, then write 0 for the remaining terms.

NOTE: Uses Kosaraju's Algorithm.
'''

import time

########################## GLOBALS #################################

finishing_times = [0 for _ in range(875715)]    # Tracks finish times
leader_node = None                              # Allows assignment of leader node to other nodes
finish_time = 0                                 # Incremented to update finishing_times
scc_sizes   = []                                # List of scc sizes

########################## FUNCTIONS ###############################


'''
Compute finishing times for each node
Uses graph with reversed edges and DFS
'''
def reverse_dfs(reversed_graph, given_node):
    """ Compute finishing times for each node.
    :param reversed_graph: Adjacency list (the given graph, but with reversed edges).
    :param given_node: Integer (represents the node which has been recursed on).
    Returns:
        The median of the three inputted integers.
    """
    
    
    # Locals

    # 1. Mark given_node as explored

    # 2. Set the leader of given_node to the global leader_node

    # 3. For each element in the adjacency list created, recurse

    # 4. Increment the finishing time

    # 5. Set global finishing time of given_node to the finishing time

    pass



'''
DFS on highest to lowest finishing times
Identify SCCs
Find SCC sizes
'''
def find_sccs(graph):
    """ Finds SCCs and their size using DFS on highest to lowest finishing times.
    :param graph: Adjacency list (the given graph).
    """

    # 1. Reset visited nodes list
    
    # 1. Identify index of largest element in finishing times list

    # 2. Based on that element, dfs to find SCC

    # 3. Calculate size of SCC, add to list of SCC sizes
    
    pass


'''
Find the median value from a list of three values
Returns the median value
'''
def find_median(first, middle, last):
    """ Finds and returns the median of three inputted values.
    :param first: Integer (first element of an array).
    :param middle: Integer (middle element of an array).
    :param last: Integer (last element of an array).
    Returns:
        The median of the three inputted integers.
    """
  
    min_value = min(first, middle, last)
    max_value = max(first, middle, last)
    if first != min_value and first != max_value:
        return first
    elif middle != min_value and middle != max_value:
        return middle
    else:
        return last

def quick_sort(array):
    """ Sorts an inputted array and counts the total number of comparisons made between elements.
    :param array: Array containing integers and no duplicates in an arbitrary order.
    Returns:
        array in non-decreasing order.
    """

    len_array = len(array)
    if len_array == 1:
        return array
    
    first_index   = 0
    last_index    = len_array - 1
    if len_array % 2 == 1:
        middle_index = (len_array // 2)
    else:
        middle_index = (len_array // 2) - 1

    first_value   = array[first_index]
    middle_value  = array[middle_index]
    last_value    = array[last_index]
    
    median_value  = find_median(first_value, middle_value, last_value)

    if median_value == first_value:
        pivot_index = first_index
    elif median_value == middle_value:
        pivot_index = middle_index
    else:
        pivot_index = last_index

    # Partition
    i = 1   # Index where elements less than the pivot ends
    pivot_array = [array[pivot_index]]
    array[pivot_index], array[0] = array[0], array[pivot_index] # Swaps pivot element with the first element

    global comparisons
    comparisons = comparisons + len_array - 1

    for j in range(1, len_array):
        if array[0] > array[j]:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    
    array[i - 1], array[0] = array[0], array[i - 1] # "Puts" pivot in place

    # Recursion
    left    = array[:i - 1]
    right   = array[i:]
    if len(left) > 1:
        left = quick_sort(left)
    if len(right) > 1:
        right = quick_sort(right)

    # Combine into final array
    array = left + pivot_array + right
    
    return(array)



########################### EXECUTE ################################


file_name_1 = "SCC.txt"    # Assigned file

# Read data from file to create an adjacency list (graph)
graph       = [[] for _ in range(875715)] 
graph_rev   = [[] for _ in range(875715)] 
with open(file_name_1) as file:
    for line in file:
        edge = line.split()
        start_index = int(edge[0])
        end_value = int(edge[1])
        graph[start_index].append(end_value)
# Read data from file to create an adjacency list (graph, but in reverse order)
with open(file_name_1) as file:
    for line in file:
        edge = line.split()
        start_index = int(edge[1])
        end_value = int(edge[0])
        graph_rev[start_index].append(end_value)


# 1. Begin loop from 875715 to 1, decreasing

    # 2. Check if the node is visited

    # 3. If not visited, dfs on that node



print(graph)
print(graph_rev)