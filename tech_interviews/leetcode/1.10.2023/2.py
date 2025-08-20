from typing import List


def insert_interval(
    intervals: List[List[int]], new_interval: List[int]
) -> List[List[int]]:
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(interval[1], merged[-1][1])
        else:
            merged.append(interval)

    return merged


intervals1 = [[1, 3], [5, 7], [8, 12]]
new_interval1 = [4, 6]

intervals2 = [[1, 3], [5, 7], [8, 12]]
new_interval2 = [4, 10]

intervals3 = [[2, 3], [5, 7]]
new_interval3 = [1, 4]


print(insert_interval(intervals1, new_interval1))
print(insert_interval(intervals2, new_interval2))
print(insert_interval(intervals3, new_interval3))
