"""
Intervals Intersection (medium)

Problem Statement
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
"""


def intersect(arr_a, arr_b):

    result = []
    i, j = 0, 0

    while i < len(arr_a) and j < len(arr_b):

        # a_overlap_b = arr_b[j][1] >= arr_a[i][0] and arr_b[j][0] <= arr_a[i][0]
        # b_overlap_a = arr_a[i][1] >= arr_b[j][0] and arr_a[i][0] <= arr_b[j][0]

        a_overlap_b = arr_a[i][0] <= arr_b[j][1] and arr_b[j][0] <= arr_a[i][0]
        b_overlap_a = arr_b[j][0] <= arr_a[i][1] and arr_a[i][0] <= arr_b[j][0]


        if a_overlap_b or b_overlap_a:
            result.append(
                [max(arr_a[i][0], arr_b[j][0]), min(arr_a[i][1], arr_b[j][1])]
            )

        if arr_a[i][1] < arr_b[j][1]:
            i += 1
        else:
            j += 1
    return result


arr1 = [[1, 3], [5, 6], [7, 9]]
arr2 = [[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
print(intersect(arr1, arr2))

arr3 = [[1, 3], [5, 7], [9, 12]]
arr4 = [[5, 10]]
# Output: [5, 7], [9, 10]
print(intersect(arr3, arr4))
