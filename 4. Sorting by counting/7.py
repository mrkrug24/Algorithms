b = [0] * 256
a = ''
c = 0

while True:
    try:
        a += input()
    except:
        break
    
a = ''.join(a.split())
 
for i in range(len(a)):
    b[ord(a[i])] += 1
 
d = ''

for i in range(256):
    if b[i] > 0:
        d += chr(i)
 
for i in range(256):
    if c < b[i]:
        c = b[i]
 
for i in range(c - 1, -1, -1):
    e = ''
    
    for j in d:
        if b[ord(j)] >= i + 1:
            e += '#'
        else:
            e += ' '
            
    print(e)
    
print(d)