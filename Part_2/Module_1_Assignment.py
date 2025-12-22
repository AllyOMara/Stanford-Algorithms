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

NOTE: This program uses Kosaraju's Algorithm.
'''

import time

########################## GLOBALS #################################

SCCs = [0, 0, 0, 0, 0]     # List of the sizes of found SCCs

########################## FUNCTIONS ###############################

'''
Creates an adjacency list
'''


'''
Compute finishing times for each node
Uses Grev (Graph with reversed edges)
'''


'''
DFS on highest to lowest finishing times
Identify SCCs
Find SCC sizes
'''


