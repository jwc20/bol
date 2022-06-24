from test_framework import generic_test


def is_palindrome(s: str) -> bool:

    left = 0
    right = len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic_punctuation.py",
            "is_string_palindromic_punctuation.tsv",
            is_palindrome,
        )
    )
