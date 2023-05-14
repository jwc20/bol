"""
Given two lists of intervals, find the intersection of these two lists. 
Each list consists of disjoint intervals sorted on their start time.


"""


def intervals_intersection(arr1, arr2):

    intersects = []
    max_range = max(len(arr1), len(arr2))
    j = 0

    for i in range(max_range):
        if arr1[i][0] <= arr2[j][1]:
            curr = [max(arr1[i][0], arr2[j][0]), min(arr1[i][1], arr2[j][1])]

    return 0


arr1 = [[1, 3], [5, 6], [7, 9]]
arr2 = [[2, 3], [5, 7]]

print(intervals_intersection(arr1, arr2))
