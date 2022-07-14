
def max_sub_array_of_size_k(k,arr):

    """
    Input: An array of numbers (integers), integer
    Output: integer

    Find max sum of any contiguous subarrays with size K.

    Naive:
        Compute the sum of all subarrays with size K and append to a list.
        Return the max of that list.
        The Python max() method adds to the time.
        O(n * K) time and O(n) space where n is the size of the input list.

    Better:
        Use sliding window to find sum.
        Set max = 0.
        We need to set the start and end of the window and use conditionals to check and update the max.
        Loop through the list until < length of input - 1
    """
    window_sum, window_start, max = 0, 0, 0


    return -1
