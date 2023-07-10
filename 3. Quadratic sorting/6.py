x = int(input())
a = [0] * x

for i in range(x):
    n = input().split()
    sname = n[0]
    name = n[1]
    mark = int(n[2]) + int(n[3]) + int(n[4])
    a[i] = (mark, sname, name)
 
m1 = 0
m2 = 0
m3 = 0
 
for i in range(x):
    if a[i][0] >= m1:
        m3 = m2
        m2 = m1
        m1 = a[i][0]
        
    elif a[i][0] >= m2:
        m3 = m2
        m2 = a[i][0]
        
    elif a[i][0] >= m3:
        m3 = a[i][0]
 
 
for i in range(x):
    if a[i][0] >= m3:
        print(a[i][1] + ' ' + a[i][2])