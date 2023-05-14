def conf(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i - 1][1] > intervals[i][0]:
            return False
    return True


i1 = [[1, 4], [2, 5], [7, 9]]
i2 = [[6, 7], [2, 4], [8, 12]]
i3 = [[4, 5], [2, 3], [3, 6]]

print(conf(i1))
print(conf(i2))
print(conf(i3))
