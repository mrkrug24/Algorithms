a = []
a = input().split()

for i in range(len(a)):
    a[i] = int(a[i])
 
k = a[1]
b = a[1]

for i in range(len(a)):
    if a[i] > k and i > 0:
        k = a[i]
 
for i in range(len(a)):
    if a[i] < b and i > 0:
        b = a[i]
 
for i in range(len(a)):
    if a[i] == k and i > 0:
        a[i] = b
        
for i in range(1, len(a)):
    print(a[i],end=" ")