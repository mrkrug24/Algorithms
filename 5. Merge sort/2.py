n = int(input())
a = list(map(int, input().split()))
 
def merge(l, r):
    a = []
    
    while len(l) > 0 and len(r) > 0:
        if l[0] <= r[0]:
            a.append(l[0])
            l.remove(l[0])
            
        else:
            a.append(r[0])
            r.remove(r[0])
            
    if len(l) > 0:
        a.extend(l)
        
    if len(r) > 0:
        a.extend(r)
        
    return a
 
def sort(Y):
    l, r, a = [], [], []
    
    if len(Y) <= 1:
        return Y
    
    else:
        m = len(Y) // 2
        
        for i in Y[:m]:
            l.append(i)
            
        for i in Y[m:]:
            r.append(i)
            
        l = sort(l)
        r = sort(r)
        a = merge(l, r)
        
        return a
    
print(*sort(a))