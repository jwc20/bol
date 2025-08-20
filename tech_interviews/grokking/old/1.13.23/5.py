

def merge(intervals):
    intervals.sort(key = lambda x: x[0])

    prev = intervals[0]
    result = []

    start = prev[0]
    end = prev[1]

    for i in range(1, len(intervals)):
        curr = intervals[i] 
        if end>= curr[0]:
            end = max(end, curr[1])
        else:
            result.append([start, end])
            start = curr[0]
            end = curr[1]

    result.append([start, end])

    return result

print(merge([[1,4], [2,5], [7,9]]))
print(merge([[6,7], [2,4], [5,9]]))
print(merge([[1,4], [2,6], [3,5]]))
