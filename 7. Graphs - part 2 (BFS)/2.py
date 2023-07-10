from collections import deque

def check(x, y, n):
    return (x < 0 or y < 0 or x >= n or y >= n) == False

def edge(a, b, x, y):
    k = [2, 2, 1, 1,-1,-1,-2,-2]
    l = [1,-1, 2,-2, 2,-2, 1,-1]
    
    for i in range(8):
        if a == x + k[i] and b == y + l[i]:
            return True
        
    return False
        
n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

a = x[0] - 1
b = x[1] - 1
c = y[0] - 1
d = y[1] - 1

if a == c and b == d:
    print(0)
    
else:
    k = [2, 2, 1, 1,-1,-1,-2,-2]
    l = [1,-1, 2,-2, 2,-2, 1,-1]
    
    v = []
    for i in range(n):
        v.append([-1] * n)
        
    v[a][b] = 0
            
    q = deque()
    q.append((a, b))

    while len(q) != 0:
        x, y = q.popleft()
        
        for i in range(8):
            if check(x + k[i], y + l[i], n) == True and v[x + k[i]][y + l[i]] == -1:
                v[x + k[i]][y + l[i]] = v[x][y] + 1
                q.append((x + k[i], y + l[i]))
                
    print(v[c][d])

if v[c][d] > 0:
    ans = [0] * n
     
    ans[0] = (c, d)
    
    for i in range(1, v[c][d] + 1):
        for j in range(n):
            for s in range(n):
                w, p = ans[i - 1]
                
                if v[j][s] == v[w][p] - 1 and edge(w, p, j, s):
                    ans[i] = (j, s)
                    break
                
    ans[v[c][d]] = (a, b)
     
    for i in range(v[c][d], -1, -1):
        a, b = ans[i]
        print(a + 1, b + 1)