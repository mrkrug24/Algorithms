n = int(input())
a = input().split()
x = int(input())

for i in range(n):
    a[i] = int(a[i])
    
k = abs(x - a[0])
l = a[0]

for i in range(n):
    u = abs(x - a[i])
    
    if u < k:
        l = a[i]
        k = u
        
print(l)