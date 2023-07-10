c = int(input())
d = input().split()

for i in range(c):
    d[i] = int(d[i])
 
a = int(input())
n = input().split()
 
for i in range(a):
    n[i] = int(n[i])
   
b = [0] * 101
 
for i in range(a):
    b[n[i]] += 1
   
for i in range(c):
    if b[i + 1] <= d[i]:
        print('no')
    else:
        print('yes')