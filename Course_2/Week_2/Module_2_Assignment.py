'''
Stanford Algorithms - Course 2 Module 2
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


fully_processed_nodes = []
processed_nodes = [1]
shortest_paths = []
possible_paths = []
connected = {}
weights = {}
MAX_RANGE = 200


def create_processed_nodes_list(size):
    """ Create list of length size + 1.
    
    Arguments:
        size: (Integer) List size.
    """
    
    global fully_processed_nodes
    fully_processed_nodes = [True]  # No node labelled "0"
    for i in range(size):
        fully_processed_nodes.append(False)


def create_shortest_path_list(size):
    """ Create list of length size + 1.
    
    Arguments:
        size: (Integer) List size.
    """

    global shortest_paths
    shortest_paths = [0]
    for i in range(size):
        shortest_paths.append(0)


def create_dictionary(file_name):
    """ Creates dictionary for edge weights between two nodes.    
    
    Arguments:
        file_name: (String) File to be read from.
    """

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
    """ Creates adjacency list from file (without weights)
    
    Arguments:
        file_name: (String) File to be read from.
        size: (Integer) Largest node number.
    """
    
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
                source_nodes[node].append(end_node)
                outgoing_edges.pop(0)
    return source_nodes


def check_connectivity(given_node, graph):
    """ Modified depth-first search (DFS). Marks connected nodes as "True".
    
    Arguments:
        given_node: (Integer) Starting node.
        graph: (Adjacency list) Represents given graph.
    """

    global fully_processed_nodes
    global MAX_RANGE
    global connected
    fully_processed_nodes[given_node] = True
    end_nodes = graph[given_node]
    if len(end_nodes) > 0:
        for i in range(len(end_nodes)):
            end_node = end_nodes[i]
            if fully_processed_nodes[end_node] == False:
                check_connectivity(end_node, graph)
    connected.update({given_node : True})


def remove_unconnected_nodes(graph, max_range):
    """ Marks unconnected nodes as "True" in processed_nodes, and empties graph at that node.
    
    Arguments:
        graph: (Adjacency list) Starting node.
        max_range: (Integer) Largest node value.
    """

    global fully_processed_nodes
    global connected
    for i in range(max_range + 1):
        if i not in connected:
            graph[i] = []
            processed_nodes[i] = True


def output():
    """ Prints final answer.
    """

    global shortest_paths
    PATH_7 = shortest_paths[7]
    PATH_37 = shortest_paths[37]
    PATH_59 = shortest_paths[59]
    PATH_82 = shortest_paths[82]
    PATH_99 = shortest_paths[99]
    PATH_115 = shortest_paths[115]
    PATH_133 = shortest_paths[133]
    PATH_165 = shortest_paths[165]
    PATH_188 = shortest_paths[188]
    PATH_197 = shortest_paths[197]
    ten_shortest_paths = f"{PATH_7},{PATH_37},{PATH_59},{PATH_82},{PATH_99},{PATH_115},{PATH_133},{PATH_165},{PATH_188},{PATH_197}"
    print(ten_shortest_paths)


def dijkstra():
    """ Uses dijkstra's shortest path algorithm to find the shortest paths of 10 given nodes.
    """

    global weights
    global shortest_paths
    global processed_nodes

    FILE_NAME_1 = "dijkstraData.txt" # Assigned file
    FILE_NAME_2 = "dijkstra-0946310.txt"
    FILE_NAME_3 = "dijkstra-39.txt"
    FILE_NAME_4 = "dijkstra-01234432.txt"
    FILE_NAME_5 = "dijkstra-03585711461010.txt"
    chosen_file = FILE_NAME_1

    graph = create_graph(chosen_file, MAX_RANGE)
    create_dictionary(chosen_file)
    create_processed_nodes_list(MAX_RANGE)
    create_shortest_path_list(MAX_RANGE)
    check_connectivity(1, graph)
    remove_unconnected_nodes(graph, MAX_RANGE)
    create_processed_nodes_list(MAX_RANGE)

    while len(processed_nodes) < MAX_RANGE:
        path_length = 0
        needs_processing = False
        for i in range(len(processed_nodes)):
            possible_parent_node = processed_nodes[i]
            child_nodes = graph[possible_parent_node]
            for i in range(len(child_nodes)):
                possible_child_index = i
                possible_child_node = child_nodes[i]
                if possible_child_node not in processed_nodes:
                    possible_path_length = weights[possible_parent_node][possible_child_node] + shortest_paths[possible_parent_node]
                    if path_length == 0 or (possible_path_length < path_length):
                        path_length = possible_path_length
                        parent_node = possible_parent_node
                        child_node = possible_child_node
                        child_index = possible_child_index
                        needs_processing = True
        if needs_processing == True:
            processed_nodes.append(child_node)
            shortest_paths[child_node] = path_length
            graph[parent_node].pop(child_index)

    output()


def main():
    dijkstra()


if __name__ == "__main__":
    main()