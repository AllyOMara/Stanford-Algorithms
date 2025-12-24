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

finishing_times = [0 for _ in range(875715)]        # Tracks finish times
visited_nodes   = [False for _ in range(875715)]    # Tracks which nodes have been visited
leader_node     = None                              # Allows assignment of leader node to other nodes
finish_time     = 0                                 # Incremented to update finishing_times
scc_sizes       = []                                # List of scc sizes

def reverse_dfs(reversed_graph, given_node):
    
    """ Compute finishing times for each node by using DFS on the reversed graph.
    :param reversed_graph: Adjacency list (the given graph, but with reversed edges).
    :param given_node: Integer (represents the node which has been recursed on).
    """

    global visited_nodes
    global finish_time
    global finishing_times
    # 1. Check if the node has been explored
    if visited_nodes[given_node] == False:
        # 1. Mark given_node as explored
        visited_nodes[given_node] = True
        # 2. For each node adjacent to the given node, recurse
        if len(reversed_graph[given_node]) != 0:
            for end_node in len(reversed_graph[given_node]):
                reverse_dfs(end_node)
        # 3. Increment the finishing time
        finish_time = finish_time + 1
        # 4. Set global finishing time of given_node to the finishing time
        finishing_times[given_node] = finish_time


def find_sccs(graph, given_node):
    
    """ Finds SCCs and their size using DFS on highest to lowest finishing times.
    :param graph: Adjacency list (the given graph).
    :param given_node: Integer (represents the given node).
    """

    # 1. Reset visited nodes list
    
    # 2. Identify index of largest element in finishing times list

    # 3. Based on that element, dfs to find SCC

    # 4. Set the leader of given_node to the global leader_node

    # 5. Calculate size of SCC, add to list of SCC sizes
    
    pass


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


def create_adj_list(size):
    
    """ Create adjacency list of length size + 1 (allows for easier indexing).
    :param size: Integer (determines adjacency list size).
    :return: List of length size + 1 (where all lists are distinct)
    """
    
    return_list = [[]]
    for i in range(size):
        return_list.append([])
    return return_list
    

def create_graphs(file_name):
    
    """ Create two adjacency lists to represent graphs - one in directed order, one in reversed order.
    :param file_name: String (determines which file will be used to create adjacency lists)
    """

    graph       = create_adj_list(875715)
    graph_rev   = create_adj_list(875715)

    with open(file_name) as file:
        for line in file:
            edge = line.split()
            start_index = int(edge[0])
            end_value = int(edge[1])
            graph[start_index].append(end_value)

    with open(file_name) as file:
        for line in file:
            edge = line.split()
            start_index = int(edge[1])
            end_value = int(edge[0])
            graph_rev[start_index].append(end_value)

    return graph, graph_rev


def main():

    MAX_RANGE = 875715
    file_name_1 = "SCC.txt"    # Assigned file

    graph, graph_rev = create_graphs(file_name_1)

    # First loop (on the reverse graph). Gets finishing times.
    for node in range(MAX_RANGE - 1, 0, -1):
        if visited_nodes[node] == False:
            reverse_dfs(graph_rev, node)

    print(finishing_times)

    # Reset visited nodes list

    # Find all the SCCs list

    # Sort the list of SCCs

    # Get 5 largest SCCs in a separate list (final answer)


if __name__ == "__main__":
    main()


'''
TO DO

x. Add function for reading data from file.
x. main() function should not do any work (eventually).

---

DONE



'''