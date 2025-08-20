"""
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all necessary
intervals to produce a list that has only mutually exclusive intervals.


"""


def insert(intervals, new_interval):
    merged = [] 
    i = 0

    while i < len(intervals):
        curr = intervals[i]

        if curr[0] < new_interval[1]:
            merged.append(min(curr[0], new_interval[0]), max(curr[1], new_interval[1]))
            
        else:
            merged.append(curr)

    




    return 0
