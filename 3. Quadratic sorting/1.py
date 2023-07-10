a = int(input())
n = input().split()

MAX = 0
 
for i in range(a):
    n[i] = int(n[i])
   
for i in range(a):
    if n[MAX] < n[i]:
        MAX = i

K = n[0]
L = n[MAX]

n[0] = L
n[MAX] = K

print(*n)