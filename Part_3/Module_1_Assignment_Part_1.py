'''
Stanford Algorithms - Part 3 Module 1
Programming Assignment

Solution by Alexandria O'Mara

TASK

This file describes a set of jobs with positive and integral
weights and lengths. It has the format:
[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...
For example, the third line of the file is "74 59", indicating
that the second job has weight 74 and length 59. You should
NOT assume that edge weights or lengths are distinct.

Run the greedy algorithm that schedules jobs in decreasing
order of the difference (weight - length). Recall from lecture
that this algorithm is not always optimal. 

IMPORTANT: if two jobs have equal difference (weight - length),
you should schedule the job with higher weight first. 
Report the sum of weighted completion times of the resulting
schedule - a positive integer.
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


def calculate_job_keys(file_name):
    """ Find each job's key (weight - length). Return array containing all keys.

    Reads the given file (file_name), and generates the key for each job. The
    key can be defined as weight minus length, and is used in this greedy
    algorithm to determine the final job ordering.
    """
    job_keys = []
    with open(file_name) as file:
        for line in file:
            job_description = line.split()
            if len(job_description) == 2:
                print(job_description)
                job_weight = int(job_description[0])
                job_length = int(job_description[1])
                job_key = int(job_weight - job_length)
                job_keys.append(job_key)
    return job_keys


def create_key_to_job_dictionary(job_keys):
    """ Loop through job_keys (array), adding the job associated with each key
    to a dictionary.

    The given array (job_keys) is looped through (for i in ...) and each
    iteration adds a new entry into the dictionary. The dictionary is later
    used to determine ordering in the greedy algorithm.
    """
    
    dictionary = {}
    for i in range(len(job_keys)):
        key = job_keys[i]
        if key not in dictionary:
            dictionary.update({key : [i]})
        else:
            dictionary[key].append(i)
    
    return dictionary
            
    

def create_weights_list(file_name):
    """ List of weights of all jobs. Returned in an array.

    Used to resolve 'ties' in keys by scheduling the job with the higher weight
    before the job with the lower weight. Returns all job weights in an array.
    """

    weights_list = []
    with open(file_name) as file:
        for line in file:
            job_description = line.split()
            if len(job_description) > 1:
                weights_list.append(int(job_description[0]))
    return weights_list


def calculate_final_schedule(key_to_job_dictionary, weights_list, sorted_keys):
    """ Returns the final schedule of jobs based on their keys.
    """

    visited_keys = []
    final_schedule = []
    for i in range(len(sorted_keys)):
        key = sorted_keys[i]
    pass




def calculate_completion_time(final_schedule):
    """ Returns the final answer (the sum of weighted completion times).

    Uses final_schedule to calculate the sum of weighted completion times, which
    is returned.
    """
    pass


def greedy():
    """ Greedy algorithm used to generate the final scheduling order of jobs.

    Main while loop (while length of scheduled jobs != max_range) to schedule
    jobs in a close-to-optimal ordering. Prints final schedule.
    If there is a clash between keys, choose the job with the highest weight 
    before the job of the lowest weight.
    **IMPORTANT NOTE**: add a case where the weights are equal.
    """
    
    FILE_NAME_1 = 'jobs.txt'
    chosen_file = FILE_NAME_1

    job_keys = calculate_job_keys(chosen_file)
    key_to_job_dicitonary = create_key_to_job_dictionary(job_keys)
    weight_list = create_weights_list(chosen_file)
    sorted_keys = quick_sort(job_keys)


def main():
    greedy()


if __name__ == "__main__":
    main()


'''
TO DO:

x. Fill in functions
x. Make small test files
x. Test on small test files

Completed:
x. Make outline ("skeleton")


'''
