b = int(input())
a = int(input())
n = input().split()

MAX = 0

if a == 0:
    print(0)
else:
    for i in range(a):
        n[i] = int(n[i])
   
    for i in range(0, a):
        for g in range(0, a - 1):
            if n[g] > n[g + 1]:
                K = n[g]
                L = n[g + 1]
                
                n[g] = L
                n[g + 1] = K
                
    c = 0
    
    if a == 0:
        print(0)
        
    if n[0] >= b:
        c = 1
        
    x = n[0]
           
    for i in range(a):
        if n[i] - x >= 3 and n[i] >= b:
            c = c + 1
            x = n[i]
            
    print(c)