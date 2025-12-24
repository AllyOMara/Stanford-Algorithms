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

finish_time     = 0                                 # Incremented to update finishing_times
scc_sizes       = []                                # List of scc sizes
file_name_1     = "SCC.txt"                         # Assigned file
MAX_RANGE       = 875714

def reverse_dfs(reversed_graph, given_node):
    
    """ Compute finishing times for each node by using DFS on the reversed graph.
    :param reversed_graph: Adjacency list (the given graph, but with reversed edges).
    :param given_node: Integer (represents the node which has been recursed on).
    """

    global visited_nodes
    global finish_time
    global finishing_times
    # 1. Mark given_node as explored
    visited_nodes[given_node] = True
    # 2. For each node adjacent to the given node, recurse
    if len(reversed_graph[given_node]) > 0:
        for end_node in range(len(reversed_graph[given_node])):
            if visited_nodes[end_node] == False:
                reverse_dfs(reversed_graph, end_node)
    # 3. Increment the finishing time
    finish_time = finish_time + 1
    # 4. Set global finishing time of given_node to the finishing time
    finishing_times[given_node] = finish_time


def find_sccs(graph, given_node):
    
    """ Finds SCCs and their size using DFS on highest to lowest finishing times.
    :param graph: Adjacency list (the given graph).
    :param given_node: Integer (represents the given node).
    """
    global visited_nodes
    global scc_sizes
    scc_size = 0
    # 1. Set given_node to visited
    visited_nodes[given_node] = True
    # 2. Based on given_node, dfs to find SCC
    for end_node in len(graph[given_node]):
        find_sccs(graph, end_node)
        scc_size = scc_size + 1
    # 3. Add scc_size to list of SCC sizes
    scc_sizes.append(scc_size)


def find_median(first, middle, last):
    
    """ 
    Find and return the median of first, middle, last.
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
    
    """ Sort array.
    :param array: Array containing integers and no duplicates in an arbitrary order.
    Returns:
        Array in non-decreasing order.
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


def create_list(size):
    
    """ Create list of length size + 1 (allows for easier indexing).
    :param size: Integer (adjacency list size).
    :return: List of length size + 1. All indexes contain the given element.
    """
    
    return_list = [[]]
    for i in range(size):
        return_list.append([])
    return return_list
    

def create_graph(file_name):
    
    """ Create adjacency list to represent graph.
    :param file_name: String (determines which file will be used to create adjacency lists).
    """

    graph       = create_list(MAX_RANGE)

    with open(file_name) as file:
        for line in file:
            edge = line.split()
            start_index = int(edge[0])
            end_value = int(edge[1])
            graph[start_index].append(end_value)

    return graph


def create_graph_rev(file_name):
    
    """ Create adjacency list to represent graph with reversed edges.
    :param file_name: String (determines which file will be used to create adjacency lists).
    """
    
    graph_rev   = create_list(MAX_RANGE)

    with open(file_name) as file:
        for line in file:
            edge = line.split()
            start_index = int(edge[1])
            end_value = int(edge[0])
            graph_rev[start_index].append(end_value)

    return graph_rev


def main():
    global visited_nodes
    finishing_times = create_list(MAX_RANGE, 0)                                     # FIX
    visited_nodes = create_list(MAX_RANGE, False)                                   # FIX
    graph, graph_rev = create_graph(file_name_1), create_graph_rev(file_name_1)

    # First loop (on the reverse graph). Gets finishing times
    for node in range(MAX_RANGE, 0, -1):
        if visited_nodes[node] == False:
            reverse_dfs(graph_rev, node)

    # Reset visited nodes list
    visited_nodes = []
    
    # Second loop (on graph). Finds SCCs
    for finished_time in range(1, MAX_RANGE):
        node = finishing_times.index(finished_time)
        if visited_nodes[node] == False:
            leader_node = node
            find_sccs(graph, node)
    # Sort the list of SCCs
    quick_sort(scc_sizes)
    # Get 5 largest SCCs in a separate list (final answer)
    largest_sccs = scc_sizes[0:5]
    print(largest_sccs)


if __name__ == "__main__":
    main()


'''
TO DO

x. Finish main()
x. main() function should not do any work (eventually).

---

DONE



'''