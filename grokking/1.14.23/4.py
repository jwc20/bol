def conflicting_appointment(intervals):
    intervals.sort(key=lambda x: x[0])

    i = 1

    while i < len(intervals):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
        i += 1

    return True


i1 = [[1, 4], [2, 5], [7, 9]]
i2 = [[6, 7], [2, 4], [8, 12]]
i3 = [[4, 5], [2, 3], [3, 6]]

print(conflicting_appointment(i1))  # => false
print(conflicting_appointment(i2))  # => true
print(conflicting_appointment(i3))  # => false
