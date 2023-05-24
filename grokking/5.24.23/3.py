def make_squares(arr):
    """
    Note that input array is sorted and we are outputting another array (=> O(n) space)

    A naive approach would be to get the absolute value for each element and sort it from there.
    Then we return the array where each element is sorted.
    This approach will give us O(nlogn) and O(n) because of the sorting.

    Another better apprach would be to use pointers from both ends of the list.
    We can compare the absolute value of the two elements and append that to a new list.

    Appending to a new list will still take O(n) space, so we can maybe reorder the existing list.

    loop while l<r:
        if l <= r, then arr[r] ** 2 and r--
        if l > r, then:
            swap,
            arr[r] = arr[l] ** 2
            l++
    """

    l, r = 0, len(arr) - 1

    while l <= r:
        if abs(arr[l]) <= abs(arr[r]):
            arr[r] = arr[r] ** 2
            r -= 1
        elif abs(arr[l]) > abs(arr[r]):
            arr[l], arr[r] = arr[r], arr[l] ** 2
            # arr[r] = arr[l] ** 2
            l += 1
            r -= 1
    return arr


def make_squares_soln(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highestSquareIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1

    return squares


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))

    print("Squares: " + str(make_squares_soln([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares_soln([-3, -1, 0, 1, 2])))


main()
