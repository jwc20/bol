
def fun(s: str) -> bool:

    start = 0
    end = len(s) - 1
    

    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and start < end:
            end -= 1 
        if s[start].lower() != s[end].lower():
            print(s[start], s[end])
            return False

        start += 1
        end -= 1


    return True




print(fun("A man, a plan, a canal, Panama."))
