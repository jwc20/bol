def fun(st):
    s = list(st)
    def reverse_word(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1

    reverse_word(s, 0, len(s) - 1)

    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != " ":
            finish += 1
        if finish == len(s):
            break
        reverse_word(s, start, finish - 1)
        start = finish + 1

    reverse_word(s, start, len(s) - 1)
    return s


print(fun("Alice likes Bob"))
