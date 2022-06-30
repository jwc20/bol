def fun(s: str) -> int:
    total = 0
    neg = False
    digit_place = 1

    split_str = list(s)

    d = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

    if s[0] == "-":
        neg = True

    for i in reversed(range(len(split_str))):
        if split_str[i] in d:
            total += d[split_str[i]] * digit_place
            digit_place *= 10

    # SHould i handle ignore when first digit is 0?

    if neg == True:
        return -1 * total

    return total


print(fun("123"))
print(fun("-123"))
print(fun("-12312312123"))
print(fun("1231231231123"))
print(fun("0"))


def fun1(x: int) -> str:
    d = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}
    neg = False
    result = []

    if x < 0:
        neg = True
        x *= -1

    while x >= 1:
        rem = x % 10
        if (rem) in d:
            result.append(d[rem])
        x = x // 10

    if neg == True:
        result.append("-")

    return ("").join(reversed(result))

    

print(fun1(-123))
print(fun1(123))
