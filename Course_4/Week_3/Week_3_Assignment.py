"""
Stanford Algorithms - Course 4 Week 3
Programming Assignment

Solution by Alexandria O'Mara

TASK
In this assignment we will revisit an old friend, the traveling salesman problem
(TSP). This week you will implement a heuristic for the TSP, rather than an
exact algorithm, and as a result will be able to handle much larger problem
sizes.

This file (nn.txt) describes a TSP instance with the structure:
[number of cities]
[city 1 index] [city 1 x coordinate] [city 1 y coordinate]
[city 2 index] [city 2 x coordinate] [city 2 y coordinate]
...

You should implement the nearest neighbor heuristic:
    1. Start the tour at the first city.
    2. Repeatedly visit the closest city that the tour hasn't visited yet.
       In case of a tie, go to the closest city with the lowest index.
    3. Once every city has been visited exactly once, return to the first city.

Find the cost of the traveling salesman tour computed by the nearest neighbor
heuristic for this instance, rounded down to the nearest integer.

NOTE: The distance between two cities is defined as the Euclidean distance.
"""