n = int(input())

a = [] * n
a = input().split()

for i in range(n):
    a[i] = int(a[i])

x = int(input())

for i in range(n):
    if a[i] == x:
        print("YES")
        break
        
    elif a[i] != x and i == n - 1:
        print("NO")