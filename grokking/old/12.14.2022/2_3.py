# from typing import List

import collections

def func(s: str, K: int) -> int:

    """
    Longest substring with K distinct characters.

    Set variable that counts up to K.
    Set variable that is the size of the resulting string.

    We can use a hashmap that has the characters as key and the count as the value for that character.

    araaci
    ^^
    {a:1, r:1}

    araaci
    ^ ^
    {a:2, r:1}
    The size of has map must be K.

    araaci
    ^  ^
    {a:3, r:1}

    araaci
    ^   ^
    {a:3, r:1} !-> {a:3, r:1, c:1}
    The length of hashmap is now 3, now we shrink the window.
    Set the max_length as 4


    araaci
     ^  ^
    {a:2, r:1} !-> {a:2, r:1, c:1}
    Shrink

    araaci
      ^ ^
    {a:2, c:1}
    Check if current subtring length is greater than max_length

    araaci
      ^  ^
    {a:2, c:1} !-> {a:2, c:1, i:1}
    Shrink

    araaci
       ^ ^
    {a:1, c:1} !-> {a:1, c:1, i:1}
    Shrink

    araaci
        ^^
    {i:1, c:1}
    Check if current subtring length is greater than max_length

    return max_length

    """

    max_length = 0
    d = {}
    window_start = 0

    for window_end in range(len(s)):
        if s[window_end] not in d:
            d[s[window_end]] = 1

        elif s[window_end] not in d and len(d) >= K:
            d[s[window_start]] -= 1
            window_start += 1
        else:
            d[s[window_end]] += 1

    return max_length


def sol(s, K):
    max_length = 0
    window_start = 0
    # d = {}
    d = collections.defaultdict(set)

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in d:
            d[right_char] = 1
        else:
            d[right_char] += 1

        while len(d) > K:
            left_char = s[window_start]
            d[left_char] -= 1
            if d[left_char] == 0:
                del d[left_char]

            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


s0 = "araaci"
k0 = 2

print(func(s0, k0))
print(sol(s0, k0))
