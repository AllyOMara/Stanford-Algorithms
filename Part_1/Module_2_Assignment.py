'''
TASK

This file (integerarray.txt) contains all of the 100,000 integers between
1 and 100,000 (inclusive) in some order, with no integer repeated.
Compute the number of inversions in the file given, where the ith row
of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast
divide-and-conquer algorithm covered in the video lectures.
'''


#################################################################################
##########################      GLOBAL VARIABLES      ###########################
#################################################################################


inv_count   = 0
input_array = []
# len_left    = None
# len_right   = None
# merged      = []


#################################################################################
##############################      FUNCTIONS      ##############################
#################################################################################


'''
Count left and right inversions.
Also sort the left and right halves (to achieve O(n*log(n))
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

    while len(left) > 0 and len(right) > 0:
        if len(right) > 0 and len(left) > 0:
            if left[0] > right[0]:
                merged.append(right[0])
                right.pop(0)
            elif left[0] < right[0]:
                merged.append(left[0])
                left.pop(0)

    if len(right) > 0:
        merged.extend(right)
    elif len(left) > 0:
        merged.extend(left)     # While the + operator can be used, since the length of the arrays are sufficiently large, .extend is used to save time
    print(left, right)
    print(merged)

    return merged


#################################################################################


file_name_1 = "integerarray.txt"
file_name_2 = "even.txt"
file_name_3 = "odd.txt"

# Read all lines in the file and place in an array
with open(file_name_2) as file:
    for line in file:
        input_array.append(int(line))
print(input_array)

sorted_array = merge_and_count(input_array)
print(sorted_array)
