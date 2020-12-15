n = int(input())
d = {
    'W': set(),
    'R': set(),
    'X': set(),
}
for i in range(n):
    input_ = input().split()
    fname = input_[0]
    permissions = input_[1:]
    for key in permissions:
        # if key == 'W':
        #    d['W'].add(fname)
        # if key == 'R':
        #    d['R'].add(fname)
        # if key == 'X':
        #    d['X'].add(fname)
        d[key].add(fname)
operations = { 
    'read' : 'R',
    'write': 'W',
    'execute': 'X',
}
for i in range(int(input())):
    op, fname = input().split()
    if fname in d[operations[op]]:
        print('OK')
    else:
        print('Access denied')