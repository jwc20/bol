def sqrt(x: int) -> int: 
    if x > 2:
        return x / (x/2) 
    else: 
        return 1


print(sqrt(8)) 
print(sqrt(4))
print(sqrt(2))
