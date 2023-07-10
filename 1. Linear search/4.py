n = int(input())

a = [] * n
a = input().split()

x = int(input())

k = a[0]
l = 0

for i in range(n):
    a[i] = int(a[i])
    
for i in range(len(a)):
    if a[i] == x:
        k = a[i]
        l = i + 1
        print(l, end =" ")