a = int(input())
n = input().split()
 
for i in range(a):
    n[i]= int(n[i])
 
b = [0] * 20001
 
for i in range(a):
    b[n[i] + 10000] += 1
 
for i in range(20001):
    for j in range(b[i]):
        print(i - 10000)