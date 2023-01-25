def merge(intervals):
    result = []

    intervals.sort(key=lambda x: x[0])

    last_interval_start = intervals[0][0]
    last_interval_end = intervals[0][1]

    for i in range(1, len(intervals)):
        # if the preceding interval's end is greater than the current interval
        # when they overlap
        if last_interval_end >= intervals[i][0]:
            last_interval_end = max(last_interval_end, intervals[i][1])

        # when they don't overlap
        else:
            result.append([last_interval_start, last_interval_end])
            last_interval_start = intervals[i][0]
            last_interval_end = intervals[i][1]

    result.append([last_interval_start, last_interval_end])

    return result


print(merge([[1, 4], [2, 5], [7, 9]]))
print(merge([[6, 7], [2, 4], [5, 9]]))
print(merge([[1, 4], [2, 6], [3, 5]]))
