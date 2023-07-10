n = int(input())
a = []

for i in range(n):
    a.append([int(j) for j in input().split()])

x, y, z = 0, 0, 0
min = 1001

for i in range(n):
    for j in range(n):
        for l in range(n):
            if l != i and l != j and i != j:
                if a[i][j] + a[i][l] + a[l][j] < min:
                    min =  a[i][j] + a[i][l] + a[l][j]
                    x, y, z = i, j, l
                   
print(x + 1, y + 1, z + 1)