'''
Stanford Algorithms - Part 1 Module 2
Programming Assignment

Solution by Alexandria O'Mara

TASK

This file (QuickSort.txt) contains all of the integers between
1 and 10,000 (inclusive, with no repeats) in unsorted order.
The integer in the ith row of the file gives you the ith entry
of an input array.
Compute the total number of comparisons used to sort the given
input file by QuickSort. As you know, the number of comparisons
depends on which elements are chosen as pivots, so we'll ask
you to explore three different pivoting rules

For the first part of the programming assignment, you should
always use the first element of the array as the pivot element.
'''

####################################################################
########################## GLOBALS #################################
####################################################################

comparisons = 0     # Count of performed comparisons

####################################################################
########################## FUNCTIONS ###############################
####################################################################

'''
Quick Sort
Count number of comparisons
'''
def quick_sort(array):
    # Return if the length of the array is 1
    len_array = len(array)
    if len_array == 1:
        return array

    # Partition A around P (i.e. get all <p to the right and all >p to the left)
    

    # Recursively sort left and right







####################################################################
########################### EXECUTE ################################
####################################################################

file_name_1 = "QuickSort.txt"       # Assigned file


# Read data from file
input_array = []
with open(file_name_1) as file:
    for line in file:
        input_array.append(int(line))
len_input = len(input_array)
print(input_array)

