import math

class Solution:
  def mySqrt(self, x: int) -> int:
    if x < 2:
      return x # return x if it is 0 or 1

    left, right = 2, x // 2 # initialize left and right pointers
    pivot = 0
    num = 0 # use int to store result of pivot * pivot to prevent overflow
    while left <= right: # binary search for the square root
      pivot = left + (right - left) // 2 # find the middle element
      num = pivot * pivot
      print(x, left, right, pivot, num)
      if num > x:
        right = pivot - 1 # if pivot * pivot is greater than x, set right to pivot - 1
      elif num < x:
        left = pivot + 1 # if pivot * pivot is less than x, set left to pivot + 1
      else:
        return pivot # if pivot * pivot is equal to x, return pivot
    return right # return right after the loop

solution = Solution()

input1 = 4
expectedOutput1 = 2
result1 = solution.mySqrt(input1)
print(result1 == expectedOutput1) # Expected output: True

input2 = 8
expectedOutput2 = 2
result2 = solution.mySqrt(input2)
print(result2 == expectedOutput2) # Expected output: True

input4 = 2
expectedOutput4 = 1
result4 = solution.mySqrt(input4)
print(result4 == expectedOutput4) # Expected output: True

input5 = 3
expectedOutput5 = 1
result5 = solution.mySqrt(input5)
print(result5 == expectedOutput5) # Expected output: True

input6 = 15
expectedOutput6 = 3
result6 = solution.mySqrt(input6)
print(result6 == expectedOutput6) # Expected output: True

print(result6)
