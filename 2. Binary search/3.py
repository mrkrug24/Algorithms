n, k = map(int,input().split())
 
a = []
a = input().split()
 
b = []
b = input().split()
 
for i in range(n):
    a[i] = int(a[i])
   
for i in range(k):
    b[i] = int(b[i])
    L = 0
    l = 0
    R = n - 1
    r = n - 1
    
    while R - L > 1:
        m = (L + R)// 2
        
        if b[i] <= a[m]:
            R = m
        else:
            L = m + 1
           
    while r - l > 1:
        m = (l + r)// 2
        if b[i] < a[m]:
            r = m - 1
        else:
            l = m
 
    if b[i] != a[l] and b [i] != a[r]:
        print(0)
       
    if b[i] == a[L] and b[i] == a[l] and b[i] != a[r]:
        print(L + 1, l + 1)
        
    if b[i] == a[L] and b[i] == a[r]:
        print(L + 1, r + 1)
        
    if b[i] == a[R] and b[i] == a[l] and b[i] != a[r] and b[i] != a[L]:
        print(R + 1, l + 1)
        
    if b[i] == a[R] and b[i] == a[r] and b[i] != a[L] and b[i] != a[L]:
        print(R + 1, r + 1)