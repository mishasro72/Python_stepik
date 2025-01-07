n, m =[int(x) for x in input().split()]
a=[[0 for i in range (m)] for j in range (n)]
x=1
i=0
j=0
a[i][j] = x
while x < n*m:
    while j < (m - 1) and a[i][j + 1] == 0:
        j+=1
        x +=1
        a[i][j] = x
    while i < (n - 1) and a[i + 1][j] == 0:
        i += 1
        x +=1
        a[i][j] = x
    while j > 0 and a[i][j - 1] == 0:
        j -= 1
        x +=1
        a[i][j] = x
    while i > 0 and a[i - 1][j] == 0:
        i -= 1
        x +=1
        a[i][j] = x
for i in range(n):
    for j in range(m):
        print(str(a[i][j]).ljust(3), end = " ")
    print()
