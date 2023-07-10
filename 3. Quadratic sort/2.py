a = int(input())
n = input().split()

MAX = 0
 
for i in range(a):
    n[i] = int(n[i])
 
for j in range(a):
    MAX = 0
    
    for i in range(a - j):
        if n[MAX] < n[i]:
            MAX = i
            
    L = n[MAX]
    n[MAX] = n[a - j - 1]
    n[a - j - 1] = L
    
print(*n)