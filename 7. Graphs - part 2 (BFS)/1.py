from collections import deque

n = int(input())

a = [[int(j) for j in input().split()] for i in range(n)]
z = [int(i) for i in input().split()]

if z[0] == z[1]:
    print(0)
    
if z[0] != z[1]:
    s = z[0] - 1
    f = z[1] - 1
    
    v = [-1] * n
    v[s] = 0
    
    q = deque()
    q.append(s)
    
    while len(q) != 0:
        u = q.popleft()
        
        for i in range(n):
            if a[i][u] == 1 and v[i] == -1:
                v[i] = v[u] + 1
                q.append(i)
     
    print(v[f])
    
    if v[f] != -1:
        ans = [0] * n
        ans[0] = f
        
        for i in range(1, v[f] + 1):
            for j in range(n):
                if v[j] == v[ans[i - 1]] - 1 and a[j][ans[i - 1]] == 1:
                    ans[i] = j
                    break
                
        ans[v[f]] = s
     
        for i in range(v[f], -1, -1):
                print(ans[i] + 1, end = " ")