import math


def longest_substring_with_k_distinct(str1: str, k: int) -> int:
    w_start = 0
    max_length = 0
    char_freq = {}

    for w_end in range(len(str1)):
        right_char = str1[w_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        while len(char_freq) > k:
            left_char = str1[w_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            w_start += 1

        max_length = max(max_length, w_end - w_start + 1)

    return max_length


print(longest_substring_with_k_distinct("araaci", 2))
