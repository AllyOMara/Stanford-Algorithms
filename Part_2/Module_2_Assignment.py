'''
Stanford Algorithms - Part 2 Module 2
Programming Assignment

Solution by Alexandria O'Mara

TASK

This file (dijkstraData.txt) contains an adjacency list
representation of an undirected weighted graph with 200
vertices labeled 1 to 200. Each row consists of the node
tuples that are adjacent to that particular vertex along
with the length of that edge.

Your task is to run Dijkstra's shortest-path algorithm
on this graph, using 1 (the first vertex) as the source
vertex, and to compute the shortest-path distances
between 1 and every other vertex of the graph. If there
is no path between a vertex v and vertex 1, we'll define
the shortest-path distance between 1 and v to be 1000000.

Output Format: You should report the shortest-path
distances to the following ten vertices, in order:
7,37,59,82,99,115,133,165,188,197.
'''

# SETUP
# List of processed nodes
visited_nodes = []
# List of computed shortest path distances for each node
shortest_paths = []
# Dictionary of edge lengths
weights = {}
# Maximum node value
MAX_RANGE = 200

file_name_1 = "dijkstraData.txt"    # Assigned file

chosen_file = file_name_1


def create_visited_nodes_list(size):

    """ Create list of length size + 1.
    :param size: Integer (list size).
    """
    
    global visited_nodes

    visited_nodes = [True]  # No node labelled "0"
    
    for i in range(size):
        visited_nodes.append(False)


def create_shortest_path_list(size):

    """ Create list of length size + 1.
    :param size: Integer (list size).
    """

    global shortest_paths

    shortest_paths = [0]

    for i in range(size):
        shortest_paths.append(0)


# Function to create dictionary - 
def create_dictionary(file_name):
    global weights
    edges = {}

    with open(file_name) as file:
        for line in file:
            edges = {}
            outgoing_edges = line.split()
            node = int(outgoing_edges[0])
            outgoing_edges.pop(0)
            while len(outgoing_edges) > 0:
                current_edge = outgoing_edges[0]
                comma_index = current_edge.index(",")
                end_node = int(current_edge[:comma_index])
                weight = int(current_edge[-(len(current_edge) - comma_index - 1):])
                edges.update({end_node: weight})
                outgoing_edges.pop(0)
            weights.update({node: edges})


def source_node_list(file_name, size):
    source_nodes = [[]]
    for i in range(size):
        source_nodes.append([])
    
    with open(file_name) as file:
        for line in file:
            outgoing_edges = line.split()
            node = int(outgoing_edges[0])
            outgoing_edges.pop(0)
            while len(outgoing_edges) > 0:
                current_edge = outgoing_edges[0]
                comma_index = current_edge.index(",")
                end_node = int(current_edge[:comma_index])
                source_nodes[end_node].append(node)
                outgoing_edges.pop(0)
    return source_nodes



def dijkstra():


# MAIN LOOP
# Setup any variables
create_visited_nodes_list(MAX_RANGE)
create_shortest_path_list(MAX_RANGE)
source_nodes = source_node_list(chosen_file, MAX_RANGE)
create_dictionary(chosen_file)
visited_nodes[1] = True                 # Start node (1) is processed

# Check (while loop) if processed vertices includes all vertices in the graph
while False in visited_nodes:
    # If false, check all outgoing edges from processed to unprocessed vertices

    # Choose the edge which minimises Dijkstra's greedy criterion (shortest path)
    # Mark node as processed
    # Update shortest path distance for the node

# OUTPUT
# Retrieve the ten vertices' shortest paths
# Print