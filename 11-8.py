# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa

# {
#     'apple': ['malum', 'pomum', 'popula'],
#     'fruit': ['baca', 'bacca', 'popum'],
#     'punishment':  ['malum', 'multa']
# }

# {
#     'malum': ['apple', 'punishment'],
#     ...
# }
n = int(input())
ed = {}
for i in range(n):
    ew, lws = input().split(' - ')
    lws = lws.split(', ')
    ed[ew] = lws

ld = {}
for ew, lws in ed.items():
    for lw in lws:
        ld[lw] = ld.get(lw, []) + [ew]

sorted_lws = sorted(list(ld.keys()))
print(len(sorted_lws))
for lw in sorted_lws:
    ews = ld[lw]
    ews.sort()
    print(lw,' - ', ', '.join(ews))