from collections import defaultdict
from typing import List


def func(fruits: List[str]) -> int:

    """
    [A, B, C, A, C]
     ^^ {A:1}
     ^  ^ {A:1, B:1}
     ^     ^ {A:1, B:1, C:1} => The length is greater than 2, shrink
        ^  ^ {B:1, C:1}
        ^     ^ {A:1, B:1, C:1} => shrink
           ^  ^ {A:1, C:1}
           ^     ^ {A:1, C:2}
    max_length = 3

    """

    window_start = 0
    max_fruit = 0
    d = defaultdict(set)

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in d:
            d[right_fruit] = 1
        else:
            d[right_fruit] += 1

        while len(d) > 2:
            left_fruit = fruits[window_start]
            d[left_fruit] -= 1
            if d[left_fruit] == 0:
                del d[left_fruit]
            window_start += 1
        max_fruit = max(max_fruit, window_end - window_start + 1)

    return max_fruit

f0 =['A', 'B', 'C', 'A', 'C']
f1 = ['A', 'B', 'C', 'B', 'B', 'C']
print(func(f0))
print(func(f1))

