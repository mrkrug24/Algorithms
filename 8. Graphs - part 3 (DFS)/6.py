n = int(input())
a = [[(j) for j in input()] for i in range(n)]

s = input().split()
n = int(s[0])
m = int(s[1])

cnt = 0
v = [-1] * n

for i in range(n):
    v[i] = [-1] * n

def dfs(x, y):
    v[x][y] = 0
    k = [0, 0, 1, -1]
    l = [1, -1, 0, 0]
    
    for i in range(4):
        if a[x + k[i]][y + l[i]] == "." and v[x + k[i]][y + l[i]] == -1:
            dfs(x + k[i], y + l[i])
            
    v[x][y] = 1
    
dfs(n - 1, m - 1)

for i in range(n):
    for j in range(n):
        if v[i][j] == 1:
            cnt += 1
print(cnt)