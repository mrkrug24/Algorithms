n = int(input())

a = [] * n
a = input().split()

for i in range(n):
    a[i] = int(a[i])
   
k = a[0]
 
for i in range(n):
    if a[i] > k:
        k = a[i]
        
print(k)