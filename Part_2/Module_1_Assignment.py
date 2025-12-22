'''
Stanford Algorithms - Part 2 Module 1
Programming Assignment

Solution by Alexandria O'Mara

TASK

This file (SCC.txt) contains the edges of a directed graph.
Vertices are labeled as positive integers from 1 to 875714.
Every row indicates an edge, the vertex label in first
column is the tail and the vertex label in second column is
the head.

Your task is to code up the algorithm from the video
lectures for computing strongly connected components (SCCs),
and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest
SCCs in the given graph, in decreasing order of sizes,
separated by commas (avoid any spaces). If your algorithm
finds less than 5 SCCs, then write 0 for the remaining terms.

NOTE: Uses Kosaraju's Algorithm.
'''

import time

########################## GLOBALS #################################

SCCs = [0, 0, 0, 0, 0]     # List of the sizes of found SCCs

########################## FUNCTIONS ###############################





'''
Compute finishing times for each node
Uses Grev (Graph with reversed edges)
'''


'''
DFS on highest to lowest finishing times
Identify SCCs
Find SCC sizes
'''




file_name_1 = "SCC.txt"    # Assigned file

# Read data from file to create an adjacency list (graph)
graph       = [[] for _ in range(875715)] 
graph_rev   = [[] for _ in range(875715)] 
with open(file_name_1) as file:
    for line in file:
        edge = line.split()
        start_index = int(edge[0])
        end_value = int(edge[1])
        graph[start_index].append(end_value)
# Read data from file to create an adjacency list (graph, but in reverse order)
with open(file_name_1) as file:
    for line in file:
        edge = line.split()
        start_index = int(edge[1])
        end_value = int(edge[0])
        graph_rev[start_index].append(end_value)

print(graph)
print(graph_rev)