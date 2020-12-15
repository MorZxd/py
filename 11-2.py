n = int(input())
d = {}
for i in range(n):
    fir, sec = input().split()
    d[fir] = sec
    d[sec] = fir
v = input()
print(d[v])
