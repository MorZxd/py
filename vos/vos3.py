N = int(input())
arr = []
for i in range(N):
    arr.append( [ i+1, int(input()) ] )

fin = []
for p in arr:
    # x = p[0]
    # y = p[1]
    x, y = p
    xx = y
    yy = N + 1 - x
    fin.append( [xx, yy ] )

fin = sorted(fin)
# fin.sort()

for p in fin:
    print(p[1])