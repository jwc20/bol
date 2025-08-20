def remove_duplicates(arr):
    """
    Since the list is sorted, we can use the two pointer apprach to get the optimal solution.
    We can start by having one pointer at the beginner of the list and the other pointer on the subsequent position.
    If the element on the right matches the other element on the left, then we increment a count value.
        Afterwards, we increment the two pointers.
    If they don't match, then increment only the right pointer.

    O(n), O(1)
    """
    count = 1
    left, right = 0, 1

    while right <= len(arr) - 1:
        if arr[left] != arr[right]:
            # print(arr[left], arr[right], count)
            count += 1
            left, right = right, right + 1

        # if arr[left] == arr[right]:
        else:
            right += 1
    return count


def remove_duplicates1(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1

    i = 0
    while i < len(arr):
        print(arr)
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def main():
    print(remove_duplicates1([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
