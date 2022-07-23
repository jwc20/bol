



def find_subarrays(A, target):
    result = []
    A.sort()

    for num in A:
        if num < target:
            result.append([num])
        

    for i in range(len(A)):
        left, right = i+1, len(A) -1 
        while left < right: 
            curr_prod = A[left] * A[right]
            if curr_prod < target:
                for j in range(right - left):
                    result.append([A[left], A[j]])
                left += 1
            else:
                right -= 1



    return result


print(find_subarrays([2,5,3,10], 30))
