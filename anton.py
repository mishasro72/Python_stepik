n = int(input())
spisok = []
anton = ['a', 'n', 't', 'o', 'n']
count = 0
for _ in range(n):
    spisok.append(input())
for s in spisok:
    for i in anton:
        if i in s:
            s = s[:s.index(i)]
            count += 1
        else:
            break
            #print(anton.find('anton'))
    if count == 5:
        print(spisok.index(s) + 1, end = " ")
    count = 0
    
    
