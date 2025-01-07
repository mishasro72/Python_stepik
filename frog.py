def frog(x, y, d):
    count = 0
    while y > x:
        count += 1
        x += d
    return count

print(frog(10, 100, 30))
    
