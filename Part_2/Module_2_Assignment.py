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
# List of computed shortest path distances for each node
# Dictionary of edge lengths


# MAIN LOOP
# Check (while loop) if processed vertices includes all vertices in the graph
    # If false, check all outgoing edges from processed to unprocessed vertices
    # Choose the edge which minimises Dijkstra's greedy criterion (shortest path)
    # Mark node as processed
    # Update shortest path distance for the node

# OUTPUT
# Retrieve the ten vertices' shortest paths
# Print