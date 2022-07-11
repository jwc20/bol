def f(s: str) -> bool:

    # print(list(s))
    d = {"{": "}", "[": "]", "(": ")"}
    d1 = {"}": "{", "]": "[", ")": "("}
    
    stack = []
    
    for i in range(len(list(s))):
        # print(s[i])
        if s[i] in d.keys():
            stack.append(s[i])
        
        elif not stack or d[stack.pop()] != s[i]:
            return False

    return True



print(f("()[]"))
print(f("()"))
print(f("([)"))
