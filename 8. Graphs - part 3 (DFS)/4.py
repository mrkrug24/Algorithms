s = input().split()
a = []
n = int(s[0])
b = int(s[1])
c = [[int(j) for j in input().split()] for i in range(b)]

for i in range(n):
    a.append([0]*n)

for i in range(b):
    a[c[i][0] - 1][c[i][1] - 1] = 1
    a[c[i][1] - 1][c[i][0] - 1] = 1
    
cnt = 0
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
        cnt += 1

if cnt != 0 or b != n - 1:
    print("NO")

if cnt == 0 and b == n - 1:
    print("YES")