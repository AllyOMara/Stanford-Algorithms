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
you to explore three different pivoting rules.

Compute the number of comparisons (as in Problem 1), using the
"median-of-three" pivot rule. I.e. Choose the pivot as follows.
Consider the first, middle, and final elements of the given array.
Identify which of these three elements is the median, and use this
as your pivot.
'''

import time

########################## GLOBALS #################################

comparisons = 0     # Count of performed comparisons

########################## FUNCTIONS ###############################

'''
Find the median value from a list of three values
Returns the median value
'''
def find_median(first, middle, last):
    """ Finds and returns the median of three inputted values.
    :param first: Integer (first element of an array).
    :param middle: Integer (middle element of an array).
    :param last: Integer (last element of an array).
    Returns:
        The median of the three inputted integers.
    """
  
    min_value = min(first, middle, last)
    max_value = max(first, middle, last)
    if first != min_value and first != max_value:
        return first
    elif middle != min_value and middle != max_value:
        return middle
    else:
        return last

def quick_sort(array):
    """ Sorts an inputted array and counts the total number of comparisons made between elements.
    :param array: Array containing integers and no duplicates in an arbitrary order.
    Returns:
        array in non-decreasing order.
    """

    len_array = len(array)
    if len_array == 1:
        return array
    
    first_index   = 0
    last_index    = len_array - 1
    if len_array % 2 == 1:
        middle_index = (len_array // 2)
    else:
        middle_index = (len_array // 2) - 1

    first_value   = array[first_index]
    middle_value  = array[middle_index]
    last_value    = array[last_index]
    
    median_value  = find_median(first_value, middle_value, last_value)

    if median_value == first_value:
        pivot_index = first_index
    elif median_value == middle_value:
        pivot_index = middle_index
    else:
        pivot_index = last_index

    # Partition
    i = 1   # Index where elements less than the pivot ends
    pivot_array = [array[pivot_index]]
    array[pivot_index], array[0] = array[0], array[pivot_index] # Swaps pivot element with the first element

    global comparisons
    comparisons = comparisons + len_array - 1

    for j in range(1, len_array):
        if array[0] > array[j]:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    
    array[i - 1], array[0] = array[0], array[i - 1] # "Puts" pivot in place

    # Recursion
    left    = array[:i - 1]
    right   = array[i:]
    if len(left) > 1:
        left = quick_sort(left)
    if len(right) > 1:
        right = quick_sort(right)

    # Combine into final array
    array = left + pivot_array + right
    
    return(array)

########################### EXECUTE ################################

file_name_1 = "QuickSort.txt"       # Assigned file
file_name_2 = "1_to_10_random.txt"  # File with numbers 1 to 10 (inclusive) in a random order
file_name_3 = "1_to_10_ordered.txt" # File with numbers 1 to 10 (inclusive) is ascending order
file_name_4 = "integerarray.txt"    # File with numbers 1 to 100000 (inclusive) in a random order

# Read data from file
input_array = []
with open(file_name_4) as file:
    for line in file:
        input_array.append(int(line))
len_input = len(input_array)

start_time = time.perf_counter()
sorted_array = quick_sort(input_array)
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"The sorted array is: {sorted_array}.")
print(f"The number of comparisons made was: {comparisons}.")
print(f"The time it took to sort {len_input} items and count the number of comparisons was: {elapsed_time} seconds.")