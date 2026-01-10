'''
Stanford Algorithms - Part 3 Module 1
Programming Assignment

Solution by Alexandria O'Mara

TASK

In this programming problem you'll code up Prim's minimum
spanning tree algorithm.

This file describes an undirected graph with integer
edge costs. It has the format:
[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874",
indicating that there is an edge connecting vertex #2
and vertex #3 that has cost -8874.
You should NOT assume that edge costs are positive, nor
should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree
algorithm on this graph. You should report the overall
cost of a minimum spanning tree.
'''


def create_graph(file_name):
    """ Creates an adjacency list of where each node is connected to.
    """


def create_visited_nodes():
    """ Creates list of size max node value containing False (to be updated
    when a node is visited)
    """


def create_edge_costs(file_name):
    """ Creates dictionary of edge costs between nodes.

    Will look something like this:
    edge_costs = { 
                    1:  1: 3,
                        2: 5,
                        7: -10
                    2:  5: 9,
                        6: 7
                 }
    """


def prim():
    """ Uses Prim's Algorithm to calculate the minimum cost spanning tree
    """