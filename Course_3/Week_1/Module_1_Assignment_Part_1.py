'''
Stanford Algorithms - Course 3 Module 1
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
    """ Sorts an inputted array.
    :param array: Array containing integers and no duplicates.
    Returns:
    Array in non-decreasing order.
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

    i = 1 # Index where elements less than the pivot ends
    pivot_array = [array[pivot_index]]
    array[pivot_index], array[0] = array[0], array[pivot_index] # Swaps first and pivot element

    for j in range(1, len_array):
        if array[0] > array[j]:
            array[i], array[j] = array[j], array[i]
            i = i + 1

    array[i - 1], array[0] = array[0], array[i - 1] # "Puts" pivot in place

    left    = array[:i - 1]
    right   = array[i:]
    if len(left) > 1:
        left = quick_sort(left)
    if len(right) > 1:
        right = quick_sort(right)

    array = left + pivot_array + right
    
    return(array)


def calculate_job_keys(file_name):
    """ Finds each job's key (weight - length). Returns array containing all keys.
    :param file_name: (String) Name of file with job descriptions.
    :returns: (Array) All keys in order of job numbering.
    """

    job_keys = []
    with open(file_name) as file:
        for line in file:
            job_description = line.split()
            if len(job_description) == 2:
                job_weight = int(job_description[0])
                job_length = int(job_description[1])
                job_key = int(job_weight - job_length)
                job_keys.append(job_key)
    return job_keys


def create_key_to_job_dict(file_name):
    """ Adds keys (weight / length) to a dictionary, where the jobs are the values.
    :param file_name: (String) Name of file with job descriptions.
    :returns: (Dictionary) Key : jobs pairs.
    """

    dictionary = {}
    line_number = 0
    with open(file_name) as file:
        for line in file:
            job_description = line.split()
            if len(job_description) > 1:
                job_weight = (int(job_description[0]))
                job_length = (int(job_description[1]))
                job_key = int(job_weight - job_length)
                line_number = line_number + 1
                if job_key not in dictionary:
                    dictionary.update({job_key : [line_number]})
                else:
                    dictionary[job_key].append(line_number)
    return dictionary


def create_weights_list(file_name):
    """ Finds weights of all jobs. Returns in an array.
    :param file_name: (String) Name of file with job descriptions.
    :returns: (Array) Weight of all jobs in an array (index represents job number).
    """

    weights_list = []
    with open(file_name) as file:
        for line in file:
            job_description = line.split()
            if len(job_description) > 1:
                weights_list.append(int(job_description[0]))
            else:
                weights_list.append(0)
    return weights_list


def create_lengths_list(file_name):
    """ Finds lengths of all jobs. Returns in an array.
    :param file_name: (String) Name of file with job descriptions.
    :returns: (Array) Length of all jobs in an array (index represents job number).
    """

    lengths_list = []
    with open(file_name) as file:
        for line in file:
            job_description = line.split()
            if len(job_description) > 1:
                lengths_list.append(int(job_description[1]))
            else:
                lengths_list.append(0)
    return lengths_list


def calculate_schedule(key_to_job_dict, weights, sorted_keys):
    """ Calculates and returns the final schedule of jobs based on their keys.
    :param key_to_job_dict: (Dictionary) Key : jobs pairs where jobs is a list.
    :param weights: (Array) Weight of all jobs.
    :param sorted_keys: (Array) All keys in non-descending order.
    :returns: (Array) Final schedule of jobs.
    """

    visited_keys = []
    final_schedule = []
    while len(sorted_keys) > 0:
        key_index = (len(sorted_keys) - 1)
        key = sorted_keys[key_index]
        sorted_keys.pop(key_index)
        if key not in visited_keys:
            jobs = key_to_job_dict[key]
            if len(jobs) == 1:
                final_schedule.append(jobs[0])
            else:
                while len(jobs) > 0:
                    for i in range(len(jobs)):
                        possible_job_weight = weights[(jobs[i])]
                        if i == 0:
                            job = jobs[i]
                            job_index = 0
                            job_weight = possible_job_weight
                        else:
                            if possible_job_weight >= job_weight:
                                job = jobs[i]
                                job_index = i
                                job_weight = possible_job_weight
                    final_schedule.append(job)
                    jobs.pop(job_index)
    return final_schedule


def calculate_completion_time(job_schedule, weights, lengths):
    """ Calculates and returns the final answer (sum of weighted completion times).
    :param job_schedule: (Array) Final schedule of jobs.
    :param weights: (Array) Weight of all jobs.
    :param lengths: (Array) Lengths of all jobs.
    :returns: (Integer) Sum of weighted completion times.
    """

    completion_time = 0
    sum_completion_times = 0
    for i in range(len(job_schedule)):
        job = job_schedule[i]
        job_weight = weights[job]
        job_length = lengths[job]
        completion_time = completion_time + job_length
        weighted_completion_time = job_weight * completion_time
        sum_completion_times = sum_completion_times + weighted_completion_time
    return sum_completion_times


def greedy():
    """ Greedy algorithm used to generate the final scheduling order of jobs.
    """

    FILE_NAME_1 = 'jobs.txt'
    FILE_NAME_2 = 'jobs_test_1.txt' # Final answer = 1147
    FILE_NAME_3 = 'jobs_test_2.txt' # Final answer = 1175612
    chosen_file = FILE_NAME_1

    job_keys = calculate_job_keys(chosen_file)
    key_to_job_dict = create_key_to_job_dict(chosen_file)
    weights = create_weights_list(chosen_file)
    lengths = create_lengths_list(chosen_file)
    sorted_keys = quick_sort(job_keys)
    job_schedule = calculate_schedule(key_to_job_dict, weights, sorted_keys)
    completion_time = calculate_completion_time(job_schedule, weights, lengths)
    print(completion_time)


def main():
    greedy()


if __name__ == "__main__":
    main()