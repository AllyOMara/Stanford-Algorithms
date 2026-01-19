'''
Stanford Algorithms - Course 2 Module 1
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
import sys


sys.setrecursionlimit(100000)

finish_time     = 0                     # Incremented
finishing_times = {}                    # Dictionary of finish times : node
scc_size        = 0                     # Tracks size of scc
scc_sizes       = []                    # Tracks scc sizes
MAX_RANGE       = 875714                # Largest node number

file_name_1     = "SCC.txt"             # Assigned file - max node is 875714
file_name_2     = "small_graph_01.txt"  # File with a small graph
file_name_3     = "small_graph_02.txt"  # File with a small, known graph
file_name_4     = "scc-33300.txt"       # Scc sizes = 3,3,3,0,0, max node = 9
file_name_5     = "scc-33110.txt"       # Scc sizes = 3,3,1,1,0, max node = 8
file_name_6     = "scc-11110.txt"       # Scc sizes = 1,1,1,1,0, max node = 4

current_file    = file_name_1


def insertion_and_deletion(array, value):
    
    """ Insert value into array, non-decreasing order.
    :param array: Array (max length 5)
    :param value: Integer (scc size)
    Returns:
        Array (length <= 5) after inserting value
    """

    if len(array) == 0:
        array.append(value)
    
    else:
        inserted = False
        for i in range(len(array)):
            if inserted == False:
                if value < array[i] or value == array[i]:
                    array.insert(i, value)
                    inserted = True
        if inserted == False:
            array.append(value)
        if len(array) > 5:
            array.pop(0)
    
    return array


def create_adj_list(size):
    
    """ Create list of length size + 1.
    :param size: Integer (adjacency list size).
    :return: List, indexes contain an empty list.
    """
    
    return_list = [[]]
    
    for i in range(size):
        return_list.append([])
    
    return return_list
    

def create_graph(file_name):
    
    """ Create graph.
    :param file_name: String (represents file).
    Returns:
        Graph.
    """

    graph = create_adj_list(MAX_RANGE)

    with open(file_name) as file:
        for line in file:
            edge = line.split()
            start_index = int(edge[0])
            end_value = int(edge[1])
            graph[start_index].append(end_value)

    return graph


def create_graph_rev(file_name):
    
    """ Create graph with reversed edges.
    :param file_name: String (determines file).
    Returns:
        Graph with reversed edges.
    """
    
    graph_rev = create_adj_list(MAX_RANGE)

    with open(file_name) as file:
        for line in file:
            edge = line.split()
            start_index = int(edge[1])
            end_value = int(edge[0])
            graph_rev[start_index].append(end_value)

    return graph_rev


def create_visited_nodes_list(size):
    
    """ Create list of length size + 1.
    :param size: Integer (list size).
    :return: List, indexes contain "False".
    """
    
    return_list = [False]
    
    for i in range(size):
        return_list.append(False)
    
    return return_list


def reverse_dfs(reversed_graph, given_node, visited_nodes):
    
    """ Compute finishing times for each node.
    :param reversed_graph: Adjacency list (reversed graph).
    :param given_node: Integer (represents node).
    :param visited_nodes: List
    """

    global finish_time
    global finishing_times

    visited_nodes[given_node] = True
    end_nodes = reversed_graph[given_node]
    
    if len(end_nodes) > 0:
        for i in range(len(end_nodes)):
            end_node = end_nodes[i]
            if visited_nodes[end_node] == False:
                reverse_dfs(reversed_graph, end_node, visited_nodes)

    finish_time = finish_time + 1
    finishing_times.update({finish_time : given_node})


def find_sccs(graph, given_node, visited_nodes):
    
    """ Finds SCCs and their size.
    :param graph: Adjacency list (given graph).
    :param given_node: Integer (represents node).
    :param visited_nodes: List.
    """

    global scc_size
    global scc_sizes

    visited_nodes[given_node] = True
    end_nodes = graph[given_node]

    for i in range(len(end_nodes)):
        end_node = end_nodes[i]
        if visited_nodes[end_node] == False:
            scc_size = scc_size + 1
            find_sccs(graph, end_node, visited_nodes)


def five_largest_sccs():
    
    """ Prints five largest sccs in non-descending order.
    """
    
    global leader
    global scc_size
    global scc_sizes
    
    start_time = time.perf_counter()
    visited_nodes = create_visited_nodes_list(MAX_RANGE)
    graph, graph_rev = create_graph(current_file), create_graph_rev(current_file)

    # First loop
    for node in range(MAX_RANGE, 0, -1):
        if visited_nodes[node] == False:
            reverse_dfs(graph_rev, node, visited_nodes)
    
    visited_nodes = create_visited_nodes_list(MAX_RANGE)
    
    # Second loop
    for finished_time in range(MAX_RANGE, 0, -1):
        node = finishing_times.get(finished_time)
        if visited_nodes[node] == False:
            scc_size = 1
            find_sccs(graph, node, visited_nodes)
            scc_sizes = insertion_and_deletion(scc_sizes, scc_size)
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"The five largest SCCs are: {scc_sizes}.")
    print(f"The time taken was: {elapsed_time} seconds.")


def main():
    five_largest_sccs()


if __name__ == "__main__":
    main()