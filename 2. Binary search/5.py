a = float(input())
n = int(input())

MIN = 0

if a > 1:
    MAX = a
else:
    MAX = 1
    
x = 0

while MAX - MIN >= 0.000000000001:
    x = (MAX + MIN) / 2
    if x ** n - a >= 0.000000000001:
        MAX = x
    else:
        MIN = x
        
if a == 0 or a == 1:
    print(a)
else:
    print(round(x, 11))