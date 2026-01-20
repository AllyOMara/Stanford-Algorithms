# Course 3

## Overview
Part 3 of Algorithms Specialization. Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming.<br><br>

## Solutions
### [Week 1 - Part 1 and Part 2](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Course_3/Week_1)<br>
Uses the greedy algorithm described in lectures to schedule jobs and find the sum of weighted completion times.<br>
Job keys were described as being difference (weight - length) in Part 1, and ratio (weight / length) in Part 2.<br>
Note that "sum of weighted completion times" can be described as the following: $\sum_{j = 1}^n w_j \cdot C_j$, where $w_j$ is the job's weight, and $C_j$ is the job's completion time (described as the sum of job lengths up to and including job $j$).<br>
#### Key Implementations
- No globals.<br>
- Dictionary usage.<br>
- Reading data from a file.<br>

### [Week 1 - Part 3: Prim's Algorithm](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Course_3/Week_1)<br>
Prim's minimum spanning tree (MST) algorithm, used for finding the minimum cost spanning tree in a graph.<br>
Finds and prints the overall cost of the MST.<br>
#### Key Implementations
- Prim's Algorithm - to find the cost of the MST in a graph.<br>
- Dictionary usage - to implement 'look-ups' in $O(1)$ time instead of $O(n)$ time.<br>

### [Week 3 - Maximum-Weight Independent Set](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Course_3/Week_3)<br>
Uses a dynamic programming algorithm to find and print whether certain vertices are within the maximum-weight independent set of the graph.<br>
Note that independent set can be defined as a subset of a given path graph where no two consecutive nodes are within the set.<br>
Maximum-weight independent sets are merely the independent set with the highest weight.<br>
#### Key Implementations
- Dynamic programming algorithm usage.<br>
- Reconstruction of nodes within an independent set.<br>
- Less hardcoding - usage of files to avoid hardcoding solutions.<br>


### [Week 4: Knapsack Problem](https://github.com/AllyOMara/Stanford-Algorithms/tree/main/Course_3/Week_4)<br>
Dynamic programming algorithm used to find an optimal solution to the Knapsack Problem.<br>
Finds and prints the overall value of the optimum knapsack.<br>
#### Key Implementations
- Dynamic programming algoruthm usage.<br>
- Usage of a testing file - using pytest.<br>
<br>