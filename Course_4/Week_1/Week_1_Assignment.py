"""
Stanford Algorithms - Course 4 Week 1
Programming Assignment

Solution by Alexandria O'Mara

TASK

In this assignment you will implement one or more algorithms for the all-pairs
shortest-path problem. Three data files (g1.txt, g2.txt, and g3.txt) describing
three graphs have the structure:
[number_of_vertices] [number_of_edges]
[first_vertex] [second_vertex] [edge_length]
...

Your task is to compute the "shortest shortest path".

Precisely, you must first identify which, if any, of the three graphs have no
negative cycles. For each such graph, you should compute all-pairs shortest
paths and remember the smallest one.

You can use whatever algorithm you like to solve this question.

NOTE: Uses the Floyd-Warshall Algorithm.
"""


def get_edge_weights(file_name):
    """ Gets edge weights from the given file, puts them into a dictionary.\n
    Dictionary structure: dictionary[node_one][node_two] = edge weight
    Arguments:
        file_name: (String) File name which contains details of the given graph. (See task details for file structure)
    Returns:
        (Dictionary) All edge weights in a dictionary with structure dict[parent][child] = weight.
    """

    weights = {}
    first_line = True
    with open(file_name) as file:
        for line in file:
            if first_line:
                first_line = False
            else:
                edge_description = line.split()
                node_1 = int(edge_description[0])
                node_2 = int(edge_description[1])
                weight = int(edge_description[2])
                if node_1 not in weights:
                    weights.update({node_1: {node_2: weight}})
                else:
                    weights[node_1].update({node_2: weight})
    return weights


def get_number_of_nodes(file_name):
    """ Reads file and returns the number of nodes.
    Arguments:
        file_name: (String) File name which contains the number of nodes in the given graph. (See task details for file structure)
    Returns:
        (Integer) The total number of nodes in the given graph.
    """

    first_line = True
    number_of_nodes = None
    with open(file_name) as file:
        for line in file:
            if first_line:
                description = line.split()
                number_of_nodes = int(description[0])
                return number_of_nodes


def get_graph(file_name, number_of_nodes):
    """ Reads file to create adjacency list of all child nodes.
    Arguments:
        file_name: (String) File name which contains the given graph. (See task details for file structure)
        number_of_nodes: (Integer) Total number of nodes in the given graph.
    Returns:
        (Adjacency list) The given graph without edge weights.
    """

    graph = []
    for i in range(number_of_nodes + 1):
        graph.append([])
    first_line = True
    with open(file_name) as file:
        for line in file:
            if first_line:
                first_line = False
            else:
                edge_description = line.split()
                node_1 = int(edge_description[0])
                node_2 = int(edge_description[1])
                graph[node_1].append(node_2)
    return graph



def create_shortest_paths_array(number_of_nodes, graph, edge_weights):
    """ Creates and returns a 3-Dimensional array.\n
    Dimensions are: (number_of_nodes + 1) x (number_of_nodes + 1) x (number_of_nodes + 1)\n
    Base cases:\n
    * when i = j, array[i][j][0] = 0
    * when edge i-j does not exist, array[i][j][0] = None
    * When edge i-j does exist, array[i][j][0] = weight of i-j edge

    Arguments:
        number_of_nodes: (Integer) Total number of nodes present in the graph.
        graph: (Adjacency list) The given graph without edge weights.
        edge_weights: (Dictionary) All edge weights in a dictionary with structure dict[parent][child] = weight.
    Returns:
        (3D Array) 3-Dimensional array with base cases accounted for.
    """

    shortest_paths_array = []
    for i in range(number_of_nodes + 1):
        shortest_paths_array.append([])
        for j in range(number_of_nodes + 1):
            shortest_paths_array[i].append([])
            for k in range(number_of_nodes + 1):
                # Base cases
                if k == 0:
                    i_child_nodes = graph[i]
                    if j in i_child_nodes:
                        weight = edge_weights[i][j]
                    else:
                        weight = None
                    if i == j:
                        shortest_paths_array[i][j].append(k)
                    else:
                        shortest_paths_array[i][j].append(weight)
                else:
                    shortest_paths_array[i][j].append(None)
    return shortest_paths_array


def floyd_warshall(number_of_nodes, shortest_paths_array):
    """ Uses the Floyd-Warshall algorithm to compute and return the shortest shortest path.
    Arguments:
        number_of_nodes: (Integer) Total number of nodes in the given graph.
        shortest_paths_array: (3D Array) Array to keep track of all shortest paths from all source nodes.
    Returns:
        (Integer) Shortest shortest path in the graph.
    """

    shortest_path = 0

    # Solving subproblems
    for k in range(1, number_of_nodes + 1):
        for i in range(1, number_of_nodes + 1):
            for j in range(1, number_of_nodes + 1):
                case_1 = shortest_paths_array[i][j][k - 1]
                case_2_part_1 = shortest_paths_array[i][k][k - 1]
                case_2_part_2 = shortest_paths_array[k][j][k - 1]
                if (case_2_part_1 == None) or (case_2_part_2 == None):
                    case_2 = None
                else:
                    case_2 = case_2_part_1 + case_2_part_2
                if (case_1 == None) and (case_2 == None):  # Both are None
                    path_length = None
                elif (case_1 != None) and (case_2 == None):  # case_1 is not None
                    path_length = case_1
                elif (case_1 == None) and (case_2 != None):  # case_2 is not None
                    path_length = case_2
                else:  # Both cases are not None
                    path_length = min(case_1, case_2)
                shortest_paths_array[i][j][k] = path_length
                if path_length != None:
                    if path_length < shortest_path:
                        shortest_path = path_length

    # Checking for negative cycle
    for node in range(1, number_of_nodes + 1):
        for n in range(1, number_of_nodes + 1):
            diagonal_value = shortest_paths_array[node][node][n]
            if diagonal_value != None:
                if diagonal_value < 0:
                    return "NULL"
    return shortest_path


def find_shortest_shortest_path():
    """ Algorithm used to find the shortest shortest path.
    """

    FILE_NAME_1 = "g1.txt"
    FILE_NAME_2 = "g2.txt"
    FILE_NAME_3 = "g3.txt"

    # First graph
    edge_weights_1 = get_edge_weights(FILE_NAME_1)
    number_of_nodes_1 = get_number_of_nodes(FILE_NAME_1)
    graph_1 = get_graph(FILE_NAME_1, number_of_nodes_1)
    shortest_paths_array_1 = create_shortest_paths_array(number_of_nodes_1, graph_1, edge_weights_1)
    answer_1 = floyd_warshall(number_of_nodes_1, shortest_paths_array_1)
    print(answer_1)

    # Second graph
    edge_weights_2 = get_edge_weights(FILE_NAME_2)
    number_of_nodes_2 = get_number_of_nodes(FILE_NAME_2)
    graph_2 = get_graph(FILE_NAME_2, number_of_nodes_2)
    shortest_paths_array_2 = create_shortest_paths_array(number_of_nodes_2, graph_2, edge_weights_2)
    answer_2 = floyd_warshall(number_of_nodes_2, shortest_paths_array_2)
    print(answer_2)

    # Third graph
    edge_weights_3 = get_edge_weights(FILE_NAME_3)
    number_of_nodes_3 = get_number_of_nodes(FILE_NAME_3)
    graph_3 = get_graph(FILE_NAME_3, number_of_nodes_3)
    shortest_paths_array_3 = create_shortest_paths_array(number_of_nodes_3, graph_3, edge_weights_3)
    answer_3 = floyd_warshall(number_of_nodes_3, shortest_paths_array_3)
    print(answer_3)


def main():
    find_shortest_shortest_path()


if __name__ == "__main__":
    main()