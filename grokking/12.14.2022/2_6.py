def func(s, k):
    """
    Given a string with lowercase letters only, if you are allowed
    to replace no more than ‘k’ letters with any letter,
    find the length of the longest substring having the same
    letters after replacement.

    Input: String="aabccbb", k=2
    Output: 5
    Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

    a a b c c b b
    ^ ^
    ^   ^
        ^ ^
        ^   ^
        ^     ^
        ^       ^

    """
    freq_map = {}
    substring_length = 0
    window_start = 0
    max_length = 0
    most_frequent_char_count = 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in freq_map:
            freq_map[right_char] = 0
        freq_map[right_char] += 1

        most_frequent_char_count = max(most_frequent_char_count, freq_map[right_char])

        if (window_end - window_start + 1 - most_frequent_char_count) > k:
            left_char = s[window_start]
            freq_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


print(func("aabccbb", 2))
print(func("abbcb", 1))
print(func("abccde", 1))
