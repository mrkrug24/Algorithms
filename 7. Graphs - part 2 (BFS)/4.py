n = int(input())
cnt = 0
a = [[int(j) for j in input().split()] for i in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            cnt += 1
 
print(int(cnt / 2))