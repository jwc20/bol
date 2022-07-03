from typing import List 

def fun(A:List[str], s: int) -> List[str]:
    result = []
    for i in range(s):
        if A[i] == 'a':
            result.append('d')
            result.append('d')
        elif A[i] == "b":
            continue
        else:
            result.append(A[i])
    return result

print(fun(["a","b","a","c","d","a","e","s","f","b"], 4))

