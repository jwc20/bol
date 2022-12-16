from collections import defaultdict


def func(s: str, k: int) -> int:
    """
    This problem is similar to the other sliding window problems with
    hashmap.
    The only drawback is that I have to know the most frequent character
    in the string to determine which characters to replace

    Examine: bccbb , k = 2
        - {b: 3, c:2}
        - b is the most frequent character
        - since there are two c's we can replace them.

        b c c b b
        ^^
        ^ ^  most_frequent_char_count = 1, max_length = 2
        ^   ^  most_frequent_char_count = 2, max_length = 3
        ^     ^ most_frequent_char_count = 2, max_length = 4
        ^       ^ most_frequent_char_count = 3, max_length = 5
    """

    window_start = 0
    max_length = 0
    most_frequent_char_count = 0
    freq_map = defaultdict(set)

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in freq_map:
            freq_map[right_char] = 0
        freq_map[right_char] += 1

        most_frequent_char_count = max(most_frequent_char_count, freq_map[right_char])

        # Shrink window if the number of characters that needs to be 
        # changed is greater than k.
        if (window_end - window_start + 1 - most_frequent_char_count) > k:
            left_char = s[window_start]
            window_start += 1
            freq_map[left_char] -= 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


s0 = "aabccbb"
k0 = 2
s1 = "abbcb"
k1 = 1
s2 = "abccde"


print(func(s0, k0))  # => 5
print(func(s1, k1))  # => 4
print(func(s2, k1))  # => 3
