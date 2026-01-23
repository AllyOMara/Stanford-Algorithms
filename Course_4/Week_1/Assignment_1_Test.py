"""
Test file for Week_1_Assignment.py

Contains 4 test cases.

"""


import Week_1_Assignment as week


def test_1():
    file_name = "test_graph_1.txt"
    edge_weights = week.create_edge_weight_dictionary(file_name)
    number_of_nodes = week.get_number_of_nodes(file_name)
    graph = week.create_adjacency_list(file_name, number_of_nodes)
    shortest_paths_array = week.create_shortest_paths_array(number_of_nodes, graph, edge_weights)
    answer = week.floyd_warshall(number_of_nodes, shortest_paths_array)
    assert answer == -41


def test_2():
    file_name = "test_graph_2.txt"
    edge_weights = week.create_edge_weight_dictionary(file_name)
    number_of_nodes = week.get_number_of_nodes(file_name)
    graph = week.create_adjacency_list(file_name, number_of_nodes)
    shortest_paths_array = week.create_shortest_paths_array(number_of_nodes, graph, edge_weights)
    answer = week.floyd_warshall(number_of_nodes, shortest_paths_array)
    assert answer == -208


def test_3():
    file_name = "test_graph_3.txt"
    edge_weights = week.create_edge_weight_dictionary(file_name)
    number_of_nodes = week.get_number_of_nodes(file_name)
    graph = week.create_adjacency_list(file_name, number_of_nodes)
    shortest_paths_array = week.create_shortest_paths_array(number_of_nodes, graph, edge_weights)
    answer = week.floyd_warshall(number_of_nodes, shortest_paths_array)
    assert answer == -431


def test_4():
    file_name = "test_graph_4.txt"
    edge_weights = week.create_edge_weight_dictionary(file_name)
    number_of_nodes = week.get_number_of_nodes(file_name)
    graph = week.create_adjacency_list(file_name, number_of_nodes)
    shortest_paths_array = week.create_shortest_paths_array(number_of_nodes, graph, edge_weights)
    answer = week.floyd_warshall(number_of_nodes, shortest_paths_array)
    assert answer == "NULL"