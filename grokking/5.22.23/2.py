def my_sqrt(x:int) -> int: 
    if x < 2: return x 
    l, r = 2, x//2          # Note: l=2 is arbitrary, it can be set to 0. 
    p, n = 0, 0
    while l <= r:
        p=l+(r-l)//2 
        n=p*p               # Since we are square rooting.
        if n>x: r=p-1 
        elif n<x: l=p+1 
        else: return p 
    return r 

print(my_sqrt(15))
