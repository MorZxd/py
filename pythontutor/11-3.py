n = int(input())
d = {}
for i in range(n):
    name, c = input().split()
    if name not in d:
        d[name] = 0
    c = int(c)
    d[name] += c
sorted_keys = sorted(list(d.keys()))
for key in sorted_keys:
    print(key, d[key])