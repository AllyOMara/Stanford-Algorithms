'''
Stanford Algorithms - Part 3 Module 1
Programming Assignment

Solution by Alexandria O'Mara

TASK

In this programming problem you'll code up Prim's minimum
spanning tree (MST) algorithm.

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
cost of a minimum spanning tree (MST).
'''


def create_graph(file_name, max_range):
    """ Creates an adjacency list of where each node is connected to.
    """
    
    graph = [[]]
    for i in range(max_range + 1):
        graph.append([])
    with open(file_name) as file:
        for line in file:
            edge_description = line.split()
            if len(edge_description) > 2:
                first_node = int(edge_description[0])
                second_node = int(edge_description[1])
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
    visited_nodes[1] = True
    return visited_nodes


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
            if len(edge_description) > 2:
                first_node = int(edge_description[0])
                second_node = int(edge_description[1])
                edge_cost = int(edge_description[2])
                if first_node not in edge_costs:
                    edge_costs.update({first_node: {second_node : edge_cost}})
                else:
                    edge_costs[first_node].update({second_node: edge_cost})
                if second_node not in edge_costs:
                    edge_costs.update({second_node: {first_node: edge_cost}})
                else:
                    edge_costs[second_node].update({first_node: edge_cost})
    return edge_costs


def prim(graph, visited_nodes_bool, edge_costs):
    """ Main while loop to find and return the cost of the minimum spanning tree
    """

    visited_nodes_list = [1]
    total_cost = 0
    while False in visited_nodes_bool:
        edge_cost = None
        child_node = None
        parent_node = None
        needs_processing = False
        # Find the cheapest edge

        for i in range(len(visited_nodes_list)):
            parent_node = visited_nodes_list[i]
            child_nodes = graph[parent_node]
            for j in range(len(child_nodes)):
                possible_child_node = child_nodes[j]
                if visited_nodes_bool[possible_child_node] == False:
                    possible_edge_cost = edge_costs[parent_node][possible_child_node]
                    if edge_cost == None or edge_cost > possible_edge_cost:
                        child_node = possible_child_node
                        edge_cost = possible_edge_cost
                        needs_processing = True
        if needs_processing == True:
            # Update total MST cost
            total_cost = total_cost + edge_cost
            # Mark node as visited
            visited_nodes_bool[child_node] = True
            visited_nodes_list.append(child_node)
    return total_cost


def mst_cost():
    """ Uses Prim's Algorithm to calculate the minimum cost spanning tree
    """
    FILE_NAME_1 = 'edges.txt'   # Assigned file, MAX_RANGE = 500
    FILE_NAME_2 = 'edges_test_1.txt' # Expected answer = -1120098
    FILE_NAME_3 = 'edges_test_2.txt' # Expected answer = 3
    MAX_RANGE = 500
    chosen_file = FILE_NAME_1

    graph = create_graph(chosen_file, MAX_RANGE)
    visited_nodes = create_visited_nodes(MAX_RANGE)
    edge_costs = create_edge_costs(chosen_file)
    total_mst_cost = prim(graph, visited_nodes, edge_costs)
    print(total_mst_cost)
    


def main():
    mst_cost()


if __name__ == "__main__":
    main()