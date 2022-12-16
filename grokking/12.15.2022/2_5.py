from collections import defaultdict


def func(s: str) -> int:
    """
    Need to use sliding window and check to see if characters are
    distinct using a hashmap.
    We have to keep track of the max_length of longest substring.
    If we see a duplicate character, we would shrink the window.

    a a b c c b b
    ^^
    ^ ^
      ^^
      ^ ^
      ^   ^
      ^     ^
            ^^
            ^ ^
            ^   ^
                ^^
    """

    window_start = 0
    max_length = 0
    freq_map = defaultdict(set)

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in freq_map:
            freq_map[right_char] = 1
        else:
            freq_map[right_char] += 1

        while freq_map[right_char] >= 2:
            left_char = s[window_start]
            window_start += 1
            freq_map[left_char] -= 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


s0 = "aabccbb"
s1 = "abbbb"
s2 = "abccde"

print(func(s0))
print(func(s1))
print(func(s2))
