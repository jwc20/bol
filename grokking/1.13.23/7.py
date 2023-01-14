class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def merge(intervals):
    # Sort the intervals by their start times
    intervals.sort(key=lambda x: x.start)

    # Initialize the result list with the first interval
    result = [intervals[0]]

    # Iterate through the rest of the intervals
    for current in intervals[1:]:
        # Get the last interval in the result list
        last = result[-1]
        # If the current interval overlaps with the last interval
        if current.start <= last.end:
            # Merge the current interval with the last interval by updating the end time of the last interval
            last.end = max(last.end, current.end)
        else:
            # If the current interval does not overlap with the last interval, add it to the result list
            result.append(current)

    return result



def main():
    print("Merged intervals: ", end="")
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
