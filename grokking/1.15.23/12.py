def isPossible(a, b, c, d):
    while c >= a and d >= b:
        if c == a and d == b:
            return True

        if c > d:
            if d > b:
                c = c % d
        elif c < d:
            if c > a:
                d = d % c
        else:
            return False

        if c == a:
            if (d - b) % c == 0:
                return True
            else:
                return False
        elif d == b:
            if (c - a) % d == 0:
                return True
            else:
                return False

    return False


print(isPossible(1, 1, 3, 5))
print(isPossible(1, 1, 2, 2))
print(isPossible(1, 1, 1, 1))
