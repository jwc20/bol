def pair_with_targetsum(arr, target_sum):
    """
    Here we are going to use two pointers.
    We can start by having two pointers at both ends of the list.
    Then, we can get the sum of the elements in their position.
    After getting the sum, we can check to see if the sum is greater or lesser than the target value.
        If the sum is greater, then we decrement the right ptr.
        Else, increment the left.
    If the sum matches the target, we return the position inside a list.
    If the loop is complete (and we dont have a match), return [-1, -1]
    """

    left, right = 0, len(arr) - 1

    while left < right:
        pair_sum = arr[left] + arr[right]
        if pair_sum > target_sum:
            right -= 1
        elif pair_sum < target_sum:
            left += 1
        else:
            return [left, right]

    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
