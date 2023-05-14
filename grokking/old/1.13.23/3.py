def happy_number(num):
    slow, fast = num, num

    while True:
        slow = find_squared_sum(slow)
        fast = find_squared_sum(find_squared_sum(fast))
        if slow == fast:
            break
    return slow == 1


def find_squared_sum(num):
    _sum = 0
    while num > 0:
        _sum += (num % 10) ** 2
        num = num // 10

    return _sum


print(happy_number(23))
