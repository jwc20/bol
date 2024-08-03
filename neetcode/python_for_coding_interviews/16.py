arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

result1 = [i + j for i, j in zip(arr1, arr2)]


print(result1)


arr = [1, 2, 3, 4, 5]
result2 = [i for i in arr if i % 2 == 0]

print(result2)
