s = input().split()
n = int(s[0])
m = int(s[1])
a = [[int(j) for j in input().split()] for i in range(n)]

cnt = 0  
v = [-1] * n

def dfs(u):
    v[u] = 0
    
    for i in range(n):
        if a[u][i] == 1 and v[i] == -1:
            dfs(i)
            
    v[u] = 1
    
dfs(m - 1)

for i in range(n):
    if v[i] == 1:
        cnt += 1
        
print(cnt)