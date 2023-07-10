a = int(input())
n = list(str(a))
print(n)
 
for i in range(4):
    n[i] = int(n[i])
   
for i in range(0, 4):
    for g in range(0, 3):
        if n[g] > n[g + 1]:
            K = n[g]
            L = n[g + 1]
            
            n[g] = L
            n[g + 1] = K
            
if n[0] == 0:
    l = 0
    
    while l < 4 and n[l] == 0:
        l += 1
        
    K = n[l]
    n[l] = n[0]
    n[0] = K
   
for i in range(4):
    print(n[i], end = "")