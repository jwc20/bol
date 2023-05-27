def valid_palindrome(s: str) -> bool:
    arr = []

    for c in s.lower(): 
        if c.isalpha():
            arr.append(c)
    # print(arr)

    left, right = 0, len(arr) - 1 

    while left < right: 
        if arr[left] != arr[right]:
            return False 

        left, right = left + 1, right - 1

    return True




print(valid_palindrome("A man, a plan, a canal, Panama!"))
print(valid_palindrome("Was it a car or a cat I saw?"))
print(valid_palindrome("cat"))
print(valid_palindrome("dood"))
