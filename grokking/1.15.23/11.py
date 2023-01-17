
# Python3 implementation of the approach
 
# importing heapq python module
# for implementing min heap
import heapq
 
# Function to return the minimized sum
 
 
def getMinSum(arr, n):
    summ = 0
    # Heap to store the elements of the array
    # and retrieve the minimum element efficiently
    pq = arr
    # creating min heap from array pq
    heapq.heapify(pq)
    # While there are more than 1 elements
    # left in the queue
    while (len(pq) > 1):
        # storing minimum element (root of min heap)
        # into minn
        minn = pq[0]
        # replacing root with last element and
        # deleting last element from min heap
        # as per deleting procedure for HEAP
        pq[0] = pq[-1]
        pq.pop()
        # maintaining the min heap property
        heapq.heapify(pq)
        # again storing minimum element (root of min heap)
        # into secondMin
        secondMin = pq[0]
        # again replacing root with last element and
        # deleting last element as per heap procedure
        pq[0] = pq[-1]
        pq.pop()
        # Update the sum
        summ += (minn+secondMin)
        # appending the summ as last element of min heap
        pq.append(minn+secondMin)
        # again maintaining the min heap property
        heapq.heapify(pq)
    return summ
 
 
# Driver Code
if __name__ == "__main__":
    # arr = [2,4,3]
    arr = [1,8,3,5]
    n = len(arr)
    print(getMinSum(arr, n))
