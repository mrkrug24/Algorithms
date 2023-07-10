x = int(input())
a = 1
b = 1
c = 1

for i in range(x):
    if a * a < b * b * b:
        c = a * a
        a += 1
        
    elif a * a > b * b * b:
        c = b**3
        b += 1
        
    else:
        c = b**3
        a += 1
        b += 1
        
print(c)