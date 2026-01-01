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
import sys

sys.setrecursionlimit(100000)
finish_time     = 0                     # Incremented to update finishing_times
file_name_1     = "SCC.txt"             # Assigned file
file_name_2     = "small_graph_01.txt"  # File with a small graph
file_name_3     = "small_graph_02.txt"  # File with a small, known graph
current_file    = file_name_1           # Easily change which file is being used
leader          = 0                     # Tracks leader node
finishing_times = {}                    # Finish times and corresponding finish times
scc_sizes       = []                    # Tracks scc sizes
MAX_RANGE       = 875714                # Largest node number


def insertion_and_deletion(array, value):
    inserted = False
    for i in range(len(array)):
        if inserted == False:    
            if value < array[i]:
                array.insert(i, value)
                inserted = True
    array.pop(0)
    return array


def create_adj_list(size):
    
    """ Create list of length size + 1 (allows for easier indexing).
    :param size: Integer (adjacency list size).
    :return: List of length size + 1. All indexes contain an empty list.
    """
    
    return_list = [[]]
    for i in range(size):
        return_list.append([])
    return return_list
    

def create_graph(file_name):
    
    """ Create adjacency list to represent graph.
    :param file_name: String (determines which file will be used to create adjacency lists).
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
    
    """ Create adjacency list to represent graph with reversed edges.
    :param file_name: String (determines which file will be used to create adjacency lists).
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
    """ Create list of length size + 1 (allows for easier indexing).
    :param size: Integer (adjacency list size).
    :return: List of length size + 1. All indexes contain "False.
    """
    
    return_list = [False]
    for i in range(size):
        return_list.append(False)
    return return_list   


def reverse_dfs(reversed_graph, given_node, visited_nodes):
    
    """ Compute finishing times for each node by using DFS on the reversed graph.
    :param reversed_graph: Adjacency list (given graph with reversed edges).
    :param given_node: Integer (represents the node which has been recursed on).
    :param visited_nodes: List
    """

    global finish_time
    global finishing_times
    # 1. Mark given_node as explored
    visited_nodes[given_node] = True
    # 2. For each node adjacent to the given node, recurse
    end_nodes = reversed_graph[given_node]
    if len(end_nodes) > 0:
        for i in range(len(end_nodes)):
            end_node = end_nodes[i]
            if visited_nodes[end_node] == False:
                reverse_dfs(reversed_graph, end_node, visited_nodes)
    # 3. Increment the finishing time
    finish_time = finish_time + 1
    # 4. Set global finishing time of given_node to the finishing time
    finishing_times.update({finish_time : given_node})


def find_sccs(graph, given_node, visited_nodes):
    
    """ Finds SCCs and their size using DFS on highest to lowest finishing times.
    :param graph: Adjacency list (the given graph).
    :param given_node: Integer (represents the given node).
    :param visited_nodes: List.
    :param leaders: List (tracks leader of each node).
    :param leader: Integer (leader node).
    """
    
    # 1. Mark current node as visited
    visited_nodes[given_node] = True
    end_nodes = graph[given_node]
    # 2. Based on given_node, dfs to find SCC
    for i in range(len(end_nodes)):
        end_node = end_nodes[i]
        if visited_nodes[end_node] == False:
            find_sccs(graph, end_node, visited_nodes)
    
    # Set leader of given_node to the given leader
    


def main():

    global leader
    global scc_sizes
    
    start_time = time.perf_counter()
    visited_nodes = create_visited_nodes_list(MAX_RANGE)
    graph, graph_rev = create_graph(current_file), create_graph_rev(current_file)

    # First loop (on the reverse graph). Gets finishing times
    for node in range(MAX_RANGE, 0, -1):
        if visited_nodes[node] == False:
            reverse_dfs(graph_rev, node, visited_nodes)

    # Reset visited nodes list
    visited_nodes = create_visited_nodes_list(MAX_RANGE)
    
    # Second loop (on graph). Finds SCCs
    for finished_time in range(MAX_RANGE, 0, -1):
        node = finishing_times.get(finished_time)
        if visited_nodes[node] == False:
            leader = node
            find_sccs(graph, node, visited_nodes)
    
    largest_sccs = scc_sizes[-5:]

    # Get 5 largest SCCs in a separate list (final answer)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"The five largest SCCs are: {largest_sccs}.")
    print(f"The time taken for these SCCs to be calculated was: {elapsed_time} seconds.")


if __name__ == "__main__":
    main()


'''
TO DO

x. main() function should not do any work (eventually).

---

DONE



'''