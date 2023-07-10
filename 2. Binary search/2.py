n, k = map(int,input().split())
 
a = []
a = input().split()
 
b = []
b = input().split()
 
for i in range(n):
    a[i] = int(a[i])
   
for i in range(k):
    b[i] = int(b[i])
    l = 0
    r = n - 1
    
    while r - l > 1:
        m = (l + r) // 2
        if b[i] < a[m]:
            r = m - 1
        else:
            l = m
            
    if b[i] == a[r] or b[i] == a[l]:
        print("YES")
    else:
        print("NO")