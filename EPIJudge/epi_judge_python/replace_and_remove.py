import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # result = []
    # for i in range(size):
    #     if s[i] == 'a':
    #         result.append('d')
    #         result.append('d')
    #     elif s[i] == "b":
    #         continue
    #     else:
    #         result.append(s[i])
    # return result


    w_i, a_c = 0, 0

    for i in range(size):
        if s[i] != "b":
            s[w_i] = s[i]
            w_i += 1
        if s[i] == "a":
            a_c += 1

    c_i = w_i - 1
    w_i += a_c - 1
    final_size = w_i + 1
    while c_i >= 0:
        if s[c_i] == "a":
            s[w_i - 1 : w_i + 1] = "dd"
            w_i -= 2
        else:
            s[w_i] = s[c_i]
            w_i -= 1
        c_i -= 1
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "replace_and_remove.py",
            "replace_and_remove.tsv",
            replace_and_remove_wrapper,
        )
    )
