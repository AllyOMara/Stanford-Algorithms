"""
Stanford Algorithms - Part 3 Module 3
Programming Assignment

Solution by Alexandria O'Mara

TASK

This file describes the weights of the vertices in a path graph (with the
weights listed in the order in which vertices appear in the path).
It has the following format:
[number_of_vertices]
[weight of first vertex]
[weight of second vertex]
...
For example, the third line of the file is "6395702," indicating that the weight
of the second vertex of the graph is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and the
reconstruction procedure) from lecture on this data set.

The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones
belong to the maximum-weight independent set? (By "vertex 1" we mean the first
vertex of the graph---there is no vertex 0.) Output an 8-bit string, where the
ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight
independent set, and 0 otherwise.
"""