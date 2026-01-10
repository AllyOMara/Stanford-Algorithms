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


def create_graph(file_name, max_range):
    """ Creates an adjacency list of where each node is connected to.
    """
    
    graph = [[]]
    for i in range(max_range):
        graph.append([])
    with open(file_name) as file:
        for line in file:
            edge_description = line.split()
            if len(edge_description) > 1:
                first_node = edge_description[0]
                second_node = edge_description[1]
                graph[first_node].append(second_node)
                graph[second_node].append(first_node)   # Added twice due to the undirected nature of the graph
    return graph


def create_visited_nodes(max_range):
    """ Creates list of size max node value containing False (to be updated
    when a node is visited)
    """
    visited_nodes = [True]  # No node '0'
    for i in range(max_range):
        visited_nodes.append(False)


def create_edge_costs(file_name):
    """ Creates dictionary of edge costs between nodes.

    Should look something like this:
    edge_costs = { 
                    1:  1: 3,
                        2: 5,
                        7: -10
                    2:  5: 9,
                        6: 7
                 }
    """
    edge_costs = {}
    with open(file_name) as file:
        for line in file:
            edge_description = line.split()
            if len(edge_description) > 1:
                first_node = edge_description[0]
                second_node = edge_description[1]
                edge_cost = edge_description[2]
                if first_node not in edge_costs:
                    edge_costs.update({first_node: {second_node : edge_cost}})
                else:
                    edge_costs[first_node].update({second_node: edge_cost})
                if second_node not in edge_costs:
                    edge_costs.update({second_node: {first_node: edge_cost}})
                else:
                    edge_costs[second_node].update({first_node: edge_cost})
    return edge_costs


def prim():
    """ Uses Prim's Algorithm to calculate the minimum cost spanning tree
    """
    FILE_NAME_1 = 'edges.txt'   # Assigned file, MAX_RANGE = 500
    MAX_RANGE = 500
    chosen_file = FILE_NAME_1

    create_graph(FILE_NAME_1, MAX_RANGE)
    create_visited_nodes(MAX_RANGE)
    create_edge_costs(chosen_file)


def main():
    prim()


if __name__ == "__main__":
    main()