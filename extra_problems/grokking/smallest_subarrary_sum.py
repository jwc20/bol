import math

def smallest_subarray_sum(arr, s):
  max_sum, window_start, window_sum, min_length = 0,0,0, math.inf

  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    while window_sum >= s:
      min_length = min(min_length, window_end - window_start + 1)
      window_sum, window_start = window_sum - arr[window_start], window_start + 1

  if min_length == math.inf: return 0
  return min_length


print(smallest_subarray_sum([2, 1, 5, 2, 3, 2], 7))
