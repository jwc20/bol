def intersect(arr1, arr2):
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        one_overlap_two = arr1[i][0] >= arr2[j][0] and arr1[i][0] <= arr2[j][1]

        two_overlap_one = arr2[j][0] >= arr1[i][0] and arr2[j][0] <= arr1[i][1]

        if one_overlap_two or two_overlap_one:
            result.append([max(arr1[i][0], arr2[j][0]), min(arr1[i][1], arr2[j][1])])

        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1

        # print(i, j, result)

    return result


print(intersect([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
