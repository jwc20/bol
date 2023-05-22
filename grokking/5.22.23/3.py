# Reverse Vowels

def rev_vowels(s: str) -> str:
    """
    We are using left and right pointers.
    """

    s_list = s.split()
    left, right = 0, len(s)-1 



    vowels = "aeiouAEIOU"

    while left < right:
        if s_list[left] in vowels and s_list[right] in vowels:
            left_vowel = s_list[left]
            right_vowel = s_list[right]

            s_list[left], s_list[right] = right_vowel, left_vowel 
            left += 1
            right -= 1
        
        elif s_list[left] in vowels:
            right -= 1 

        elif s_list[right] in vowels:
            left += 1

        else:
            left += 1
            right -=1

    return s_list



def rev_vowels1(s: str) -> str:
    f, l = 0, len(s)-1 
    v = "aeiouAEIOU" 
    arr = list(s)

    while f<l:
        while f<l and v.find(arr[f]) == -1:
            f += 1
        while f<l and v.find(arr[l]) == -1:
            l -= 1 

        arr[f], arr[l] = arr[l], arr[f]
        f, l = f+1, l-1

    return "".join(arr)
        


print(rev_vowels1("DesignGUrus"))

