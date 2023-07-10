a = input()
b = input()
 
x = len(a)
y = len(b)
 
aa = [0] * 30
aaa = [0] * 10
 
bb = [0] * 30
bbb = [0] * 10
 
for i in range(x):
    if ord('0') <= ord(a[i]) <= ord('9'):
        aaa[ord(a[i]) - ord('0')] += 1
    else:
        aa[ord(a[i]) - ord('a')] += 1
 
for i in range(y):
    if ord('0') <= ord(b[i]) <= ord('9'):
        bbb[ord(b[i]) - ord('0')] += 1
    else:
        bb[ord(b[i]) - ord('a')] += 1
 
if aa == bb and aaa == bbb:
    print('YES')
else:
    print('NO')