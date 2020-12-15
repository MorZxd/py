from collections import defaultdict
n = int(input())
d = defaultdict(lambda: 0)
for i in range(n):
    name, c = input().split()
    c = int(c)
    d[name] += c
sorted_keys = sorted(list(d.keys()))
for key in sorted_keys:
    print(key, d[key])