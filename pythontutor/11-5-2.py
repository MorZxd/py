n = int(input())
d = {}

# from collections import defaultdict
# d = defaultdict(set)

for i in range(n):
    fname, *permissions = input().split()
    d[fname] = set(permissions)
operations = { 
    'read' : 'R',
    'write': 'W',
    'execute': 'X',
}
for i in range(int(input())):
    op, fname = input().split()
    if operations[op] in d.get(fname, set()):
        print('OK')
    else:
        print('Access denied')