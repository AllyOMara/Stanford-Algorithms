'''
TASK

This file (IntegerArray.txt) contains all of the 100,000 integers between
1 and 100,000 (inclusive) in some order, with no integer repeated.
Compute the number of inversions in the file given, where the ith row
of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast
divide-and-conquer algorithm covered in the video lectures.
    
'''

# Read all lines in the file and place in an array
# fd = open("integerarray.txt", "r")
len_left    = None
len_right   = None
inv_count   = 0
array       = []
merged      = []

file_name_1 = "integerarray.txt"
file_name_2 = "even.txt"
file_name_3 = "odd.txt"

with open(file_name_2) as file:
    for line in file:
        print(line[:-1])
        array.append(int(line))
print(array)

# Merge sort with count of inversions
'''
Count left and right inversions.
Also sort the left and right halves (to achieve O(n*log(n))
'''
def merge_and_count(array, inv_count):
    # Creating leaves
    len_array   = len(array)
    half_array  = len_array // 2
    left        = array[:half_array]
    right       = array[half_array:]
    len_left    = len(left)
    len_right   = len(right)
    if len_left == 1:
        pass
    elif len_left != 1:
        left = merge_and_count(left, inv_count)
    if len_right == 1:
        pass
    elif len_right  != 1:
        right = merge_and_count(right, inv_count)
    # Sorting and counting
    for i in range(len(left)):
        if len(right) != 0:
            if left[i] > right[0] and len(right) != 0:
                inv_count = inv_count + 1
                merged.append(right[0])
                right.pop(0)
            elif left[i] < right[0] and len(right) != 0:
                merged.append(left[i])
        else:
            merged.append(left[i])

    return merged

print(merge_and_count(array, inv_count))
