s = input().split()
n = int(s[0])
b = int(s[1])

a = []

for i in range(n):
    a.append([0] * n)

c = [[int(j) for j in input().split()] for i in range(b)]
 
for j in range(b):
    a[c[j][0] - 1][c[j][1] - 1] = 1
    a[c[j][1] - 1][c[j][0] - 1] = 1
   
for i in range(n):
    print(*a[i])
