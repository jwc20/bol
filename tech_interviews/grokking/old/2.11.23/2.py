def merge(intervals):
    result = []

    intervals.sort(key=lambda x: x[0])

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if end >= intervals[i][0]:
            end = max(end, intervals[i][1])

        else:
            result.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]

    result.append([start, end])

    return result


print(merge([[1, 4], [2, 5], [7, 9]]))
print(merge([[6, 7], [2, 4], [5, 9]]))
print(merge([[1, 4], [2, 6], [3, 5]]))
