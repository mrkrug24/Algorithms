n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

k, c = 0, 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            k += 1
            
v = [-1] * n

def dfs(u):
    v[u] = 0
    
    for i in range(n):
        if a[u][i] == 1 and v[i] == -1:
            dfs(i)
            
    v[u] = 1
    
dfs(0)

for i in range(n):
    if v[i] == -1:
        c += 1

if c != 0 or int(k / 2) != n - 1:
    print("NO")

if c == 0 and int(k / 2) == n - 1:
    print("YES")