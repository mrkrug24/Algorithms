n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
 
cnt = 0

for i in range(n):
    cnt = 0
    
    for j in range(n):
        if a[i][j] == 1:
            cnt += 1
            
    print(cnt)