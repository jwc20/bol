

def max_sum_subarray(nums, k):
    max_sum = 0 
    window_sum = 0
    
    for i in range(len(nums) - k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += nums[j]
        max_sum = max(window_sum, max_sum)

    return max_sum 


n1 = [2, 1, 5, 1, 3, 2]
k1=3 
n2 = [2, 3, 4, 1, 5]
k2=2 


print(max_sum_subarray(n1,k1))
print(max_sum_subarray(n2,k2))
