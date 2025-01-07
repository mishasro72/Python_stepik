def frog_jump(x, y, d):
    count = 0
    while x < y:
        x += d
        count += 1
    return count


print(frog_jump(10, 100, 30))

