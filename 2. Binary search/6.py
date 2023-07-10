a = float(input())

MIN = 0
MAX = a

while MAX - MIN >= 0.00000001:
    x = (MAX + MIN) / 2
    
    if x ** 2 + x ** 0.5 - a >= 0.00000001:
        MAX = x
    else:
        MIN = x
        
print(round(x, 7))