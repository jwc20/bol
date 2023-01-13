def merge_intervals(intervals):
    """
    To merge overlapping intervals in a list, you can use the following approach:

    Sort the list of intervals in increasing order based on the start time of each interval.
    Initialize an empty result list and a variable to store the start time of the current merged interval.
    Iterate over the sorted intervals. For each interval, do the following:
    If the current interval does not overlap with the previous interval, add a new merged interval to the result list with the start time equal to the start time of the current interval and the end time equal to the end time of the current interval.
    If the current interval overlaps with the previous interval, update the end time of the current merged interval to be the maximum of the end time of the current interval and the end time of the previous interval.
    Return the result list.
    Here is an example of how you can implement this approach in Python:
    """
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the result list and the current merged interval
    merged = []
    current_interval = intervals[0]

    # Iterate over the sorted intervals
    for interval in intervals[1:]:
        # If the current interval does not overlap with the previous interval, add a new merged interval to the result list
        if interval[0] > current_interval[1]:
            merged.append(current_interval)
            current_interval = interval
        # If the current interval overlaps with the previous interval, update the end time of the current merged interval
        else:
            current_interval[1] = max(interval[1], current_interval[1])

    # Add the final merged interval to the result list
    merged.append(current_interval)

    return merged


intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
merged_intervals = merge_intervals(intervals)
print(merged_intervals)  # [[1, 4], [5, 8]]

print(merge_intervals([[1, 4], [2, 5], [7, 9]]))
