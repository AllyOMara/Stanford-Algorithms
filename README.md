<div align="center">

# Stanford Algorithms Specialization Course Solutions
##### Learn To Think Like A Computer Scientist. Master the fundamentals of the design and analysis of algorithms. <br>
Contains solutions to selected programming assignments.

[![Coursera](https://img.shields.io/badge/cousera-blue.svg?style=for-the-badge&logo=coursera)](https://www.coursera.org/specializations/algorithms)
[![Algorithms Illuminated](https://img.shields.io/badge/Algorithms_Illuminated-darkblue.svg?style=for-the-badge&logo=none)](https://www.algorithmsilluminated.org/)
______________________
</div>
<br>

## Parts (Courses)
[Part 1- Divide and Conquer, Sorting and Searching, and Randomized Algorithms](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Part_1)<br><br>
[Part 2 - Graph Search, Shortest Paths, and Data Structures](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Part_2)<br><br>
[Part 3 - Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Part_3)<br><br>
<br>

## References
Useful resources on learning the Python programming language and designing and implementation of algorithms can be found below.
- [Algorithms Illuminated](https://www.algorithmsilluminated.org/)<br><br>
- [Learning Python *5th Ed*](https://www.amazon.com.au/Learning-Python-Mark-Lutz/dp/1449355730)<br><br>
- [Introduction to Algorithms *3rd Ed*](https://www.amazon.com.au/Introduction-Algorithms-Thomas-Dartmouth-College/dp/0262033844)<br><br>
- [Mathematics for Computer Science](https://www.amazon.com.au/Mathematics-Computer-Science-Lehman-Eric/dp/9888407066)<br><br>
- [Coursera- Stanford University Algorithms Specialization Course](https://www.coursera.org/specializations/algorithms)<br><br>
- [An Introduction to Algorithmic Thinking](https://www.lulu.com/shop/georgia-gouros/an-introduction-to-algorithmic-thinking-algorithmics-hess-student-guide/paperback/product-mnvzpy.html?page=1&pageSize=4)<br><br>
<br>

## Notable Implementations

### [MergeSort](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Part_1)<br>
Print the number of inversions present in a given array of arbitrary size and order. To ensure a fast run time (namely O(nlogn), MergeSort is employed.<br>
Note that an inversion is where two consecutive integers, i and j, exist in an array such that i > j when the list should be non-decreasing.<br>
See Module_2_Assignment.py<br>
#### Key Implementations
- MergeSort - sorting of an array in non-decreasing order.<br>
- Recursion usage - in MergeSort.
- Usage of global variable to count number of inverses.<br>
- Reading data from a file.<br>

### [Optimised QuickSort](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Part_1)<br>
QuickSort, where the pivot is chosen as the median of three elements (the first, middle, and last element in an array).<br>
Counts number of comparisons made between elements in an array.<br>
The aim of choosing the median of three elements increases the chance of an optimal 25-75 split (which is 'good enough for $O(nlogn)$').<br>
See Module_3_Assignment_Part_3.py<br>
#### Key Implementations
- QuickSort - sorting of an array in non-decreasing order.<br>
- Recursion usage - in QuickSort.<br>
- Usage of global variable to count number of comparisons.<br>
- Reading data from a file.<br>

### [Kosaraju's Algorithm](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Part_2)<br>
Kosaraju's Algorithm, used for finding the sizes of SCCS (strongly connected components) in a given graph.<br>
Finds size of five largest SCCS, prints final answer.<br>
See Module_1_Assignment.py<br>
#### Key Implementations
- Setting recursion limit - using import sys.<br>
- Modified Insertion Sort - limits array size to 5, buts keeps the array sorted.<br>
- Depth-First Search (DFS) usage to search for SCCS.<br>
- Usage of `if __name__ == "__main__"` and main() function.<br>
- Docstring usage.<br>

### [Dijkstra's Algorithm](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Part_2)<br>
Dijkstra's Algorithm, used for finding the shortest paths from a starting node to all other connected nodes in a graph.<br>
Finds and prints the shortest path from the start node (1) to ten other nodes (7,37,59,82,99,115,133,165,188,197).<br>
See Module_2_Assignment.py<br>
#### Key Implementations
- Dijkstra's Algorithm - to find shortest paths from a starting node to ten other nodes.<br>
- Dictionary usage - to implement 'look-ups' in $O(1)$ time instead of $O(n)$ time.<br>
- Modified DFS - to check for connected nodes, so unconnected nodes can be ignored.<br>

### [Prim's MST Algorithm](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Part_3)<br>
Prim's minimum spanning tree (MST) algorithm, used for finding the minimum cost spanning tree in a graph.<br>
Finds and prints the overall cost of the MST.<br>
See Part_3/Module_1_Assignment_Part_3.py<br>
#### Key Implementations
- Prim's Algorithm - to find the cost of the MST in a graph.<br>
- Dictionary usage - to implement 'look-ups' in $O(1)$ time instead of $O(n)$ time.<br>
<br>
