c9 = []
c10 = []
c11 = []

while True:
    try:
        a = input().split()
        
        if a[0] == '9':
            c9.append(a)
            
        if a[0] == '10':
            c10.append(a)
            
        if a[0] == '11':
            c11.append(a)
           
    except:
        break
    
for i in range(len(c9)):
    print(*c9[i])
    
for i in range(len(c10)):
    print(*c10[i])
    
for i in range(len(c11)):
    print(*c11[i])