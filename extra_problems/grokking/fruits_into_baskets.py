def fruits_into_baskets(A):

    w_start = 0
    max_length = 0
    char_freq = {}

    for w_end in range(len(A)):
        right_char = A[w_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        while len(char_freq) > 2:
            left_char = A[w_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            w_start += 1
        max_length = max(max_length, w_end - w_start + 1)

    return max_length


print(fruits_into_baskets(["A", "B", "C", "A", "C"]))
