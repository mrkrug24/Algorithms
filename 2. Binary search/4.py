w, h, n = map(int,input().split())
 
m = 0
   
if w > h:
    MIN = h
    MAX = n * w
    
if w < h:
    MIN = w
    MAX = n * h
    
if w == h:
    MIN = h
    MAX = n * w
 
while MAX - MIN != 0:
    m = (MAX + MIN) // 2
    if n <= (m//w) * (m//h):
        MAX = m
    else:
        MIN = m + 1
 
print(MIN)