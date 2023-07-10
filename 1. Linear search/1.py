n = int(input())

a = [] * n
a = input().split()

for i in range(n):
    a[i] = int(a[i])
    
x = int(input())
k = 0

for i in range(n):
    if a[i] == x:
        k = k + 1
        
print(k)