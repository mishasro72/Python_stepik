def counter(a, b):
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    return b

stroka = input()
answer = {}
print(counter(stroka, answer))
