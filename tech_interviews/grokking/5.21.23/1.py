def is_pangram(sentence: str) -> bool: 
    seen = set() 

    for c in sentence.lower(): 
        # seen.add(c)
        if c.isalpha():
            seen.add(c)

    return len(seen) == 26


print(is_pangram("hello"))
print(is_pangram("TheQuickBrownFoxJumpsOverTheLazyDog"))
