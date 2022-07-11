class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        input: two strings
        output: bool

        this looks like a stacks problem.

        Naive Approach is to iterate through both strings and perform the backspace and compare the two strings.

        Using the stack approach we can have two stacks and push and pop following the LIFO principle. Afterwards, check to see if string is equal.

        7 min
        """
