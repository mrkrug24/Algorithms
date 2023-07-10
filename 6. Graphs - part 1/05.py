n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
 
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and i >= j:
            print(i + 1, j + 1)