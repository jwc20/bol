def merged(arr):
    arr.sort(key = lambda x: x[0])

    merged = []
    p_st = arr[0][0]
    p_end = arr[0][1]

    for i in range(1, len(arr)):
        if p_end >= arr[i][0]:
            p_end = max(p_end, arr[i][1])

        else:
            # merged.append(arr[i])
            merged.append([p_st, p_end])
            p_st = arr[i][0]
            p_end = arr[i][1]

        
    merged.append([p_st, p_end])
    return merged


print(merged([[1,4], [2,5], [7,9]]))
print(merged([[6,7], [2,4], [5,9]]))
print(merged([[1,4], [2,6], [3,5]]))
