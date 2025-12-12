'''
TASK

This file (integerarray.txt) contains all of the 100,000 integers between
1 and 100,000 (inclusive) in some order, with no integer repeated.
Compute the number of inversions in the file given, where the ith row
of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast
divide-and-conquer algorithm covered in the video lectures.
'''

import time

inv_count   = 0
input_array = []
start_time  = time.perf_counter()

'''
Count left and right inversions.
Also sort the left and right halves (to achieve O(nlogn))
'''
def merge_and_count(array):

    len_array   = len(array)
    half_array  = len_array // 2
    left        = array[:half_array]
    right       = array[half_array:]
    len_left    = len(left)
    len_right   = len(right)

    if len_left > 1:
        left = merge_and_count(left)
    if len_right > 1:
        right = merge_and_count(right)

    merged = []
    global inv_count

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            merged.append(right[0])
            right.pop(0)
            inv_count = inv_count + len(left) # UNSURE
        elif left[0] < right[0]:
            merged.append(left[0])
            inv_count = inv_count + len(right)
            left.pop(0)

    if len(right) > 0:
        merged.extend(right)
    elif len(left) > 0:
        merged.extend(left)

    return merged

#################################################################################

file_name_1 = "integerarray.txt"    # Assigned file
file_name_2 = "even.txt"            # File with an even number integers
file_name_3 = "odd.txt"             # File with an odd number of integers
file_name_4 = "36_inv.txt"          # File with 36 inverses

# Read all lines in the file and place in an array
with open(file_name_4) as file:
    for line in file:
        input_array.append(int(line))
len_input = len(input_array)

sorted_array    = merge_and_count(input_array)
end_time        = time.perf_counter()
elapsed_time    = end_time - start_time

print(f"The sorted array is: {sorted_array}.")
print(f"The number of inverses present in the file is: {inv_count}.")
print(f"The time it took to sort {len_input} items and count the number of inverses was: {elapsed_time} seconds.")