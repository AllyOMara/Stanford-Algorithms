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

Your task is to compute the "shortest shortest path". Precisely, you must first
identify which, if any, of the three graphs have no negative cycles.

For each such graph, you should compute all-pairs shortest paths and remember
the smallest one.

You can use whatever algorithm you like to solve this question.
"""


def get_edge_weights(file_name):
    """ Reads file to retrieve edge weights, which are put into a dictionary.
    Dictionary structure: dictionary[node_one][node_two] = edge weight
    """


def get_number_of_nodes(file_name):
    """ Reads file and returns the number of nodes.
    """


def create_shortest_paths_array(number_of_nodes):
    """ Creates and returns a 3-Dimensional array.
    number_of_nodes x number_of_nodes x number_of_nodes
    """


def floyd_warshall(edge_weights, number_of_nodes):
    """ Uses the Floyd-Warshall algorithm to compute all-pairs shortest paths.
    Computes and returns shortest shortest path.
    """


def shortest_shortest_path():
    """ Algorithm used to find the shortest shortest path
    """


"""
TO DO:
x. Make test cases <-- priority
x. Fill out functions

~~~

Completed
x. Make skeleton

"""