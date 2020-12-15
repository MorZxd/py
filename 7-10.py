a = [int(i) for i in input().split()]
minn = 0
maxx = 0
for i in range(1, len(a)):
    if (a[i] > a[maxx]):
        maxx = i
    if (a[i] < a[minn]):
        minn = i
a[maxx], a[minn] = a[minn], a[maxx]
a = [str(i) for i in a]
print(' '.join(a))