from collections import deque

Q = [int(j) for j in input().split()]
q = deque()
x = Q[0]
y = Q[1]

a = [[int(j) for j in input().split()] for i in range(x)]
b = [[0, 1], [1, 0], [0, -1], [-1, 0]]
v = []

for i in range(x):
    v.append([-1] * y)

for i in range(x):
    for j in range(y):
        if a[i][j] == 1:
            v[i][j] = 0
            q.append((i, j))

while len(q) != 0:
    k, l = q.popleft()
    
    for i in range (4):
        if 0 <= k + b[i][0] < x and 0 <= l + b[i][1]  and y > l + b[i][1]:
            if v[k + b[i][0]][l + b[i][1]] == -1:
                v[k + b[i][0]][l + b[i][1]] = v[k][l] + 1
                q.append((k + b[i][0], l + b[i][1]))
 
for i in range(x):
    print(*v[i])