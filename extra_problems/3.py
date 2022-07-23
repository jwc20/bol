



def func(A):
    """
    Sliding window: O(n^2), O(n)
    First sort the array. => O(n log(n))
    
    We will get the sum of the window and compare it with the maximum_sum.
        if the window sum is greater, then set that to maximum_sum.
            We will then add the next element.
        else, continue adding.
    

    Once we reach of the end of the list with the end of the window, 
    subtract the beginning of the window and reset the window end.

    """

    left, right = 0, 1
    w_sum = 0
    max_sum = 0

    for i in range(len(A)):
        w_sum += A[]
    

    return A 





arr1 = [-2,-3,4,-1,-2,1,5,-3]


print(func(arr1)) # => 7
