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
belong to the maximum-weight independent set (IS)? (By "vertex 1" we mean the
first vertex of the graph---there is no vertex 0.) Output an 8-bit string, where
the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight
independent set, and 0 otherwise.
"""


def create_node_weights(file_name):
    """ Reads file and returns array containing all node weights
    """


def calculate_is_weight():
    """ Recurses on itself to compute the total weight of the optimal IS.
    * Recursively compute max weight IS of G' (one node removed)
    * Recursively compute max weight IS of G'' (two nodes removed) (with first node)
    * Return best max weight IS
    * Maintain array (A) (try not to make it global) to store solved subprob sizes

    i.e: A[0] = 0, A[1] = w1, for i = 2,3,...,n, A[i] = max{A[i-1], A[i-2] + wi}.
    """

    # Set array A to empty
    # Base case - empty graph - return nothing              # TODO: check base cases
    # Base case - one vertex - return vertex weight in A    # TODO: check base cases
    # Begin for loop (from i = 2 to i = n)
        # Recurse on G'
        # Recurse on G''


def reconstruct_is():
    """ Uses the array A from calculate_is_weight to output the max weight IS.
    Scans A from right to left to see which nodes are added to the mas weight IS.
    """

    # Get the filled in array A
    # Set i to the length of A
    # Set the solution (the IS) to an empty list
    # Iterate from right to left (i.e. while i >= 1)
        # If A[i - 1] >= A[i - 2] + wi  (i.e. Case 1 wins)
            # Decrease i by 1
        # Else                          (i.e. Case 2 wins)
            # Add vi to S
            # Decrease i by 1
    # Return S


def output():
    """ Check if a set of vertices are within the max weight IS    
    """

    # Initialise empty array A
    # Check if the set vertices are in the max weight IS    # TODO: Create separate file with set vertices to iterate through
        # If within max weight IS:
            # Add 1 to an array
        # If not within max weight IS:
            # Add 0 to an array
    # Return A


def max_weight_is():
    """ Calls other functions
    """


def main():
    max_weight_is()


if __name__ == "__main__":
    main()