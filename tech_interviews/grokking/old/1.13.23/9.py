def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    last_interval = intervals[0]
    for i in range(1, len(intervals)):
        if last_interval[1] > intervals[i][0]:
            return False
        last_interval = intervals[i]
    return True


def main():
    print(
        "Can attend all appointments: "
        + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]]))
    )
    print(
        "Can attend all appointments: "
        + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]]))
    )
    print(
        "Can attend all appointments: "
        + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]]))
    )


main()
