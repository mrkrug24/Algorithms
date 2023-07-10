a = int(input())
n = input().split()
 
for i in range(a):
    n[i] = int(n[i])

b = [0] * 108
c = n[0]

for i in range(a):
    if c > n[i]:
        c = n[i]
        
for i in range(a):
    b[n[i] - c] += 1

for i in range(108):
    if b[i] != 0:
        print(*b[i] * ([c + i]), end = ' ')