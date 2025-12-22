'''
Stanford Algorithms - Part 1 Module 3
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

import time

########################## GLOBALS #################################

comparisons = 0     # Count of performed comparisons

########################## FUNCTIONS ###############################

'''
Quick Sort
Count number of comparisons
'''
def quick_sort(array):
    
    len_array = len(array)
    if len_array == 1:
        return array
    
    # Partition
    i       = 1   # Index where elements less than the pivot ends
    pivot   = [array[0]]
    global comparisons
    comparisons = comparisons + len_array - 1

    for j in range(1, len_array):
        if array[0] > array[j]:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    
    array[i - 1], array[0]  = array[0], array[i - 1] # "Puts" pivot in place
    left                    = array[:i - 1]
    right                   = array[i:]

    # Recursion
    if len(left) > 1:
        left = quick_sort(left)
    if len(right) > 1:
        right = quick_sort(right)

    # Combine into final array
    array = left + pivot + right
    
    return(array)

########################### EXECUTE ################################

file_name_1 = "QuickSort.txt"       # Assigned file
file_name_2 = "1_to_10.txt"         # File with numbers 1 to 10 (inclusive) in a random order
file_name_3 = "integerarray.txt"    # File with numbers 1 to 100000 (inclusive) in a random order


# Read data from file
input_array = []
with open(file_name_1) as file:
    for line in file:
        input_array.append(int(line))
len_input = len(input_array)

start_time = time.perf_counter()
sorted_array = quick_sort(input_array)
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"The sorted array is: {sorted_array}.")
print(f"The number of comparisons made was: {comparisons}.")
print(f"The time it took to sort {len_input} items and count the number of inverses was: {elapsed_time} seconds.")