def insert(intervals, new_interval):
    result = []
    i = 0

    # when they dont overlap
    while i < len(intervals) and new_interval[0] > intervals[i][1]:
        result.append(intervals[i])
        i += 1

    # when they overlap
    while i < len(intervals) and new_interval[1] >= intervals[i][0]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    # add the remaining intervals
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


print(insert(intervals1, new_interval1))
print(insert(intervals2, new_interval2))
print(insert(intervals3, new_interval3))
