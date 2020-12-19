arr = input().split()
a = set()
for s in arr:
    if s in a:
        print('YES')
    else:
        print('NO')
        a.add(s)
#    c = len(a)
#    a.add(s)
#    r = len(a)
#    if (c == r):
#        print('YES')
#    else:
#        print('NO')