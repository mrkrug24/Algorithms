n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

cnt = 0

for i in range(n):
    for j in range(n):
        if i == j and a[i][i] == 1:
            cnt += 1
        if a[i][j] != a[j][i]:
            cnt += 1
 
if cnt != 0:      
    print("YES")
else:
    print("NO")