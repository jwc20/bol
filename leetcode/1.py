def checkPerfectNumber(num: int) -> bool:
    # divisors = []

    _sum = 0
    for i in range(1, num):
        if num % i == 0:
            # divisors.append(i)
            _sum += i
    return _sum == num

print(checkPerfectNumber(28))
print(checkPerfectNumber(7))
