def intersection(arr1, arr2):
    result = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        a_overlap_b = arr1[i][0] <= arr2[j][1] and arr1[i][0] >= arr2[j][0]
        b_overlap_a = arr1[i][1] >= arr2[j][0] and arr1[i][0] <= arr2[j][0]

        if a_overlap_b or b_overlap_a:
            result.append([max(arr1[i][0], arr2[j][0]), min(arr1[i][1], arr2[j][1])])

        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1
    return result


arr1 = [[1, 3], [5, 6], [7, 9]]
arr2 = [[2, 3], [5, 7]]


arr3 = [[1, 3], [5, 7], [9, 12]]
arr4 = [[5, 10]]

print(intersection(arr1, arr2))
print(intersection(arr3, arr4))
