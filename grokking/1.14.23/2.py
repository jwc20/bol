"""
Insert Interval (medium)

Problem Statement
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
"""

def insert_interval(intervals, new_interval):

    result = []
    i = 0

    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    result.append(new_interval)

    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result


intervals1 = [[1, 3], [5, 7], [8, 12]]
new_interval1 = [4, 6]

intervals2 = [[1, 3], [5, 7], [8, 12]]
new_interval2 = [4, 10]

intervals3 = [[2, 3], [5, 7]]
new_interval3 = [1, 4]

print(insert_interval(intervals1, new_interval1))  # Output: [[1,3], [4,7], [8,12]]
print(insert_interval(intervals2, new_interval2))  # Output: [[1,3], [4,12]]
print(insert_interval(intervals3, new_interval3))  # Output: [[1,4], [5,7]]
