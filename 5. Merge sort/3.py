a = int(input())
b = list(map(int, input().split()))
x = set(b)
 
c = int(input())
d = list(map(int, input().split()))
y = set(d)
 
if x == y:
    print("YES")
else:
    print("NO")