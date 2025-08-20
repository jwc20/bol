




"""
Problem 1:
Take two string and check to see if same in case insensitive way.

Input: two strings 
Output: boolean

The Naive Approach that comes to mind is to iterate through both strings and check each characters at a position.
We need to check to see if the length is same.

(Adding to the Naive)Another way is to use a pointer where it points to the same position in both strings.

ptr = 0
while ptr < len(s1):
    if the character at position ptr for both strings is not the same, return False
return True

This will take O(n) time.

Problem 2
Return false if the edit distance is more than 1

Should we use the Python ord() method?
ord(char) - 96

=> dont know



(12 min problem 1, 36 min total)

"""


def f(s1:str, s2:str) -> bool:
    ptr = 0 
    # if len(s1) != len(s2):
    #     return False
    while ptr < len(s1):
        if s1[ptr].lower() != s2[ptr].lower() or abs(ord(s1[ptr].lower()) - ord(s2[ptr].lower())) > 1:
            return False
        ptr += 1
    return True


s1 = "input"
s2 = "input"
s3 = "asdas"
s4 = "inpu"
s5 = "Input"

# print(f(s1,s2))
# print(f(s3,s2))
# print(f(s4,s2))
# print(f(s1,s5))

print(f("abc","ABC")) #=> True
print(f("abc","def")) #=> False
print(f("abc","ABCD")) #=> True
print(f("abc","AC")) #=> True
# print(ord("a")- 96)
# print(ord("b"))
# print(ord("z")-96)
