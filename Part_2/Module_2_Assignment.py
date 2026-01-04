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

FILE_NAME_1 = "dijkstraData.txt" # Assigned file

chosen_file = FILE_NAME_1


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


def create_graph(file_name, size):
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


def output():
    global shortest_paths

    PATH_7 = {shortest_paths[7]}
    PATH_37 = {shortest_paths[37]}
    PATH_59 = {shortest_paths[59]}
    PATH_82 = {shortest_paths[82]}
    PATH_99 = {shortest_paths[99]}
    PATH_115 = {shortest_paths[115]}
    PATH_133 = {shortest_paths[133]}
    PATH_165 = {shortest_paths[165]}
    PATH_188 = {shortest_paths[188]}
    PATH_197 = {shortest_paths[197]}
    ten_shortest_paths = f"{PATH_7},{PATH_37},{PATH_59},{PATH_82},{PATH_99},{PATH_115},{PATH_133},{PATH_165},{PATH_188},{PATH_197}"

    print(ten_shortest_paths)


def dijkstra():
    global weights
    global visited_nodes
    global shortest_paths
    
    # MAIN LOOP
    # Setup any variables
    graph = create_graph(chosen_file, MAX_RANGE)
    create_visited_nodes_list(MAX_RANGE)
    create_shortest_path_list(MAX_RANGE)
    create_dictionary(chosen_file)
    visited_nodes[1] = True # Start node (1) is processed

    # Check (while loop) if processed vertices does not include all vertices in the graph
    while False in visited_nodes:
        edge_length = 0
        # Check all outgoing edges from processed to unprocessed vertices
        for parent_node in range(len(graph)):
            if visited_nodes[parent_node] == True:
                needs_processing = False
                child_nodes = graph[parent_node]
                for i in range(len(child_nodes)):
                    possible_child_node = child_nodes[i]
                    if visited_nodes[possible_child_node] == False:
                        # Choose the edge which minimises Dijkstra's greedy criterion (shortest path)
                            possible_edge_length = weights[parent_node][possible_child_node]
                            if edge_length == 0:
                                edge_length = possible_edge_length
                            elif possible_edge_length < edge_length:
                                edge_length = possible_child_node
                                child_node = possible_child_node
                                needs_processing = True
                # Mark node as processed
                if needs_processing == True:
                    visited_nodes[child_node] = True
                    # Update shortest path distance for the node
                    shortest_paths[child_node] = shortest_paths[parent_node] + edge_length

    # OUTPUT
    # Retrieve the ten vertices' shortest paths (7,37,59,82,99,115,133,165,188,197)
    output()



def main():
    dijkstra()


if __name__ == "__main__":
    main()



'''
TO DO:

x. Create smaller test files
x. Fix main loop (under dijkstra())


Completed:

x. Make output() function - prints final answer

'''