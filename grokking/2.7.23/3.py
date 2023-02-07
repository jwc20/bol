

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [] 

    new_interval_start = intervals[0][0]
    new_interval_end= intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= new_interval_end:
            # overlap 
            new_interval_end = max(intervals[i][1], new_interval_end)
        else:
            result.append([new_interval_start, new_interval_end])
            new_interval_start= intervals[i][0]
            new_interval_end = intervals[i][1]


    result.append([new_interval_start, new_interval_end])
    return result




print(merge([[1,4], [2,5], [7,9]]))
print(merge([[6,7], [2,4], [5,9]]))
print(merge([[1,4], [2,6], [3,5]]))
