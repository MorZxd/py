n = int(input())
d = {}
for i in range(n):
    for s in input().split():
        d[s] = d.get(s, 0) + 1
mx = max(d.values())
#lst = []
#for item in d:
#    if d[item] == mx:
#        lst.append(item)
lst = [item for item in d if d[item] == mx]
mn = min(lst)
print(mn)