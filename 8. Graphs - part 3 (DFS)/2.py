n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

for i in range (n):
    for j in range (n):
        if a[i][j] == 0:
            a[i][j] = 1000000
            
        if a[i][j] == 1:
            a[i][j] = -10
            
for i in range (n):
    for j in range (n):
        for s in range (n):
            if a[j][s] > a[j][i] + a[i][s]:
                a[j][s] = a[j][i] + a[i][s]
                
for i in range (n):
    if a[i][i] < 0:
        print ("1")
        break
    
if i == n - 1:
    print ("0")