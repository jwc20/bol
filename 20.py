class Solution:
    def isValid(self, s: str) -> bool:
        # If there is only one type of paren., then use a variable and increment and decrement that
        # Then go through the characters and if at the end the variable is not equal to 0, then we have a unbalanced paren. in the string.

        # Else, use stack.
        # Go through character by character and push them onto the stack if the character is a parenthese.
        # At each character, look at the top character on the stack.
        # if it matches the closing character, pop the item off the stack.
        # At the end, check if the length of the stack is 0
        # if not, it is an unbalanced parentheses
        # if yes, it is valid
        # => O(n) time, O(n) space

        parentheses = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        # inverts the mapping
        # { ")" : "(", ... }
        inverted_parentheses = {v: k for k, v in parentheses.items()}

        stack = []
        for char in s:
            if char in parentheses:
                stack.append(char)
            elif char in inverted_parentheses:
                if len(stack) == 0 or stack[-1] != inverted_parentheses[char]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0


print(Solution().isValid("()"))
# => True

print(Solution().isValid("()[]{}"))
# => True

print(Solution().isValid("(]"))
# => False

print(Solution().isValid("(){([])}"))
# => True

print(Solution().isValid("(){(["))
# => False
