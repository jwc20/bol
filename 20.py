class Solution:
    def isValid(self, s: str) -> bool:
        # How many different parentheses are there?
            # If there is only one type of paren., then use a variable and increment and decrement that
                # Then go through the characters and if at the end the variable is not equal to 0, then we have a unbalanced paren. in the string.
            # Else, use stack.
                # Go through character by character and push them onto the stack.
                # At each character, look at the top character on the stack.
                    # if it matches the closing character, pop the item off the stack.
                # At the end, check if the length of the stack is 0
                    # if not, it is an unbalanced parentheses 
                    # if yes, it is valid
                # O(n) time, O(n) space









        return
