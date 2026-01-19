# Course 2

## Overview
Part 2 of Algorithms Specialization. Graph Search, Shortest Paths, and Data Structures.<br><br>

## Solutions
### [Week 1 - Kosaraju's Algorithm](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Course_2/Week_1)<br>
Kosaraju's Algorithm, used for finding the sizes of SCCS (strongly connected components) in a given graph.<br>
Finds size of five largest SCCS, prints final answer.<br>
See Module_1_Assignment.py<br>
#### Key Implementations
- Setting recursion limit - using import sys.<br>
- Modified Insertion Sort - limits array size to 5, buts keeps the array sorted.<br>
- Depth-First Search (DFS) usage to search for SCCS.<br>
- Usage of if __name__ == "__main__" and main() function.<br>
- Docstring usage.<br>

### [Week 2 - Dijkstra's Algorithm](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Course_2/Week_2)<br>
Dijkstra's Algorithm, used for finding the shortest paths from a starting node to all other connected nodes in a graph.<br>
Finds and prints the shortest path from the start node (1) to ten other nodes (7,37,59,82,99,115,133,165,188,197).<br>
See Module_2_Assignment.py<br>
#### Key Implementations
- Dijkstra's Algorithm - to find shortest paths from a starting node to ten other nodes.<br>
- Dictionary usage - to implement 'look-ups' in O(1) time instead of O(n) time.<br>
- Modified DFS - to check for connected nodes, so unconnected nodes can be ignored.<br>
<br>