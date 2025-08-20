def ideal_numbers(low, high):
    count = 0
    for num in range(low, high+1):
        if (num % 3 == 0 and num % 5 == 0): 
            print(num)
            count += 1
    return count


print(ideal_numbers(200, 405))

