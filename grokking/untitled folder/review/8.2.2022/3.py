

"""
Problem Statement
==================================================
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
==================================================
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".


Solution
==================================================
- need to keep a running count of length.
- A naive approach would use hashmap that will use extra O(n) space.
- Since we are returning the longest substring that is contiguous, when we get the character that is distinct from the already gotten k characters, we stop the loop.

- The sliding window solution will use hashmap, if the character we get during iteration is unique, set that as key and let it equal 1.
=> O(n) time and space
"""

def f(str1: str, k: int) -> int:
    window_start, max_length = 0,0
    d = {}

    for window_end in range(len(list(str1))):
        right = str1[window_end]
        if right not in d:
            d[right] = 0
        d[right] += 1

        while len(d) > k:
            left = str1[window_start]
            d[left] -= 1
            if d[left] == 0:
                del d[left]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

print(f("araaci", 2))
