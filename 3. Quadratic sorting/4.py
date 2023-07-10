a = int(input())
n = input().split()

MAX = 0
x = 0

for i in range(a):
    n[i] = int(n[i])
   
for i in range(0, a):
    for g in range(0, a - 1):
        if n[g] > n[g + 1]:
            K = n[g]
            L = n[g + 1]
            
            n[g] = L
            n[g+1] = K
            
            x = x + 1
            
print(x)