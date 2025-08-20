def find_happy_number(num):

    slow, fast = num, num

    while slow > 1:
        fast = get_squared_sum(get_squared_sum(fast))
        slow = get_squared_sum(slow)

        if slow == fast:
            break

    return slow == 1


def get_squared_sum(num):
    sum = 0

    while num > 0:
        digit_squared = (num % 10) ** 2
        sum += digit_squared
        num //= 10
    return sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
