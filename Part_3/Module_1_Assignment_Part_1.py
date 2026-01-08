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


def calculate_job_keys(file_name):
    """ Find each job's key (weight - length). Return array containing all keys.

    Reads the given file (file_name), and generates the key for each job. The
    key can be defined as weight - length, and is used in this greedy
    algorithm to determine the final job ordering.
    """
    pass


def create_key_to_job_dictionary(job_keys):
    """ Loop through job_keys (array), adding the job associated with each key
    to a dictionary.

    The given array (job_keys) is looped through (for i in ...) and each
    iteration adds a new entry into the dictionary. The dictionary is later
    used to determine ordering in the greedy algorithm.
    """
    pass


def create_weights_list(file_name):
    """ List of weights of all jobs. Returned in an array.

    Used to resolve 'ties' in keys by scheduling the job with the higher weight
    before the job with the lower weight. Returns all job weights in an array.
    **IMPORTANT NOTE**: ensure to add a case where the weights are equal.
    """


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
    """
    pass



'''
TO DO:

x. Fill in functions
x. Make small test files
x. Test on small test files

Completed:
x. Make outline ("skeleton")


'''
