def func(s):

    """
    Given a string, find the length of the longest substring,
    which has all distinct characters.

    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring with distinct characters is "abc".

    Need to take:
        - max_length
        - dictionary of characters (hashmap)


    for loop window_end through length of string
        check if character exists in dictionary and has value of 1
            if true, take note of the length
            else, shrink window from left

    a a b c c b b
    ^^  {a:1}       max_length =1
    ^ ^ {a:2} Shrink
      ^^    {a:1}   max_length = 1
      ^ ^   {a:1, b:1}  max_length = 2
      ^   ^ {a:1, b:1, c:1}, max_length = 3
      ^     ^   {a:1, b:1, c:2} shrink
        ^     ^   {b:2, c:1} shrink
    """

    max_length = 0
    window_start = 0
    d = {}

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in d:
            d[right_char] = 1
        else:
            d[right_char] += 1

            while d[right_char] < 1:
                left_char = s[window_start]
                left_char += 1
                if d[left_char] == 0:
                    del d[left_char]

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def sol(s):
    window_start = 0
    max_length = 0
    d = {}

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in d:
            window_start = max(window_start, d[right_char] + 1)
        d[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


s0 = "aabccbb"
print(func("aabccbb"))
print(sol("aabccbb"))
