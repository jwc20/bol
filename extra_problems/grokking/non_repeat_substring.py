def non_repeat_substring(str):
    w_st, max_length = 0, 0
    char_freq = {}
    for w_end in range(len(str)):
        right_ch = str[w_end]
        if right_ch not in char_freq:
            char_freq[right_ch] = 0
        char_freq[right_ch] += 1

        while char_freq[right_ch] > 1:
            left_ch = str[w_st]
            char_freq[left_ch] -= 1
            w_st += 1
        max_length = max(max_length, w_end - w_st + 1)
    return max_length


print(non_repeat_substring("aabccbb"))
print(non_repeat_substring("abbbb"))
print(non_repeat_substring("abccde"))
