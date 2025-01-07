n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(1), end = " ")
    print()

print(matrix)
