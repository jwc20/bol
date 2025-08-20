from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    l = len(s)
    i = 0
    while i < len(t):
        if t[i:i+l] == s:
            return i
        i += 1
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
