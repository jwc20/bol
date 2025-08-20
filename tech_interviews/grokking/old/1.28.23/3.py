def insert(intervals, new):

    results = []

    i = 0

    while i < len(intervals) and intervals[i][0] < new[0]:
        results.append(intervals[i])
        i += 1

    while i < len(intervals) and new[1] >= intervals[i][0]:
        new[1] = max(intervals[i][1], new[1])
        new[0] = min(intervals[i][0], new[0])
        i += 1

    results.append(new)

    while i < len(intervals):
        results.append(intervals[i])
        i+= 1

    return results


def main():
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6]))
    )
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10]))
    )
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[2, 3], [5, 7]], [1, 4]))
    )


main()
