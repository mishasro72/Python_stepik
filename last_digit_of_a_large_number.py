# n1 = 4
# n2 = 0

def cycle_len(n1, n2):
    if n2 == 0:
        return 1
    else:
        seen = set()
        last_dig = n1 % 10
        cycle = []
        power = n1
        while last_dig not in seen:
            seen.add(last_dig)
            cycle.append(last_dig)
            power *= n1
            last_dig = power % 10
        return cycle[n2 % len(cycle) - 1]

# print(cycle_len(n1, n2))
# print (4 ** 0)

#ver. 2
# def cycle_len(n1, n2):
#     pow(n1, n2, 10)
