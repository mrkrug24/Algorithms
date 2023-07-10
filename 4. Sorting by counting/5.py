a = int(input())
b = list(input())

c = [0] * 27
e = ''
 
for d in b:
    c[ord(d) - 65] += 1
 
for d in range(27):
    if c[d] % 2 == 1:
        if e == '':
            e = chr(d + 65)
            
        c[d] = c[d] - 1
 
f = e

for d in range(26, -1, -1):
    while c[d] > 0:
        f = chr(d + 65) + f + chr(d + 65)
        c[d] = c[d] - 2
 
print(f)