"""
leecode length of the last word
"""

def func(s):
    count = 0
    for c in reversed(s):
        if c == " " and count > 0:
            return count

        elif c == " " and count == 0:
            continue
        else: 
            count += 1 

    return count


print(func("Hello Wolrd"))
print(func("HelloWolrd"))
print(func("Hello Wolrd abcv"))
print(func("HelloWolrdabcv      "))
print(func("HelloW olrdabcv      "))
print(func("HelloWolrdabc v      "))
