def find_happy_number(num):
    fast, slow = num, num
    while fast:
        fast = calc_squared_sum(calc_squared_sum(fast))
        slow = calc_squared_sum(slow)
        if slow == fast:
            break
    return slow == 1


def calc_squared_sum(n):
    _sum = 0
    while n > 0:
        digit = n % 10
        digit_squared = digit**2
        _sum += digit_squared
        n //= 10
    return _sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
