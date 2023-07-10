x = int(input())
n = int(input())
a = []
 
for i in range(n):
    b = input().split()
    a.append([])
    
    for k in range(n):
        a[i].append(int(b[k]))
   
for i in range(n):
    for k in range(n):
        if a[k][i] == x:
            print("YES")
            break
        
    if a[k][i] != x:
        print("NO")