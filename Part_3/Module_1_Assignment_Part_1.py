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
NOT assume that edge weights or lengths are distinct. Run the
greedy algorithm that schedules jobs in decreasing order of the
difference (weight - length). Recall from lecture that this
algorithm is not always optimal. IMPORTANT: if two jobs have
equal difference (weight - length), you should schedule the job
with higher weight first. Report the sum of weighted completion
times of the resulting schedule - a positive integer.
'''
