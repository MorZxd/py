a = []
x = False
for i in range(8):
    a.append([int(i) for i in input().split()])
for item1 in a:
    for item2 in a:
        if not x:
            if (item1[0] == item2[0]) and (item1[1] != item2[1]):
                x = True
            elif (item1[0] != item2[0]) and (item1[1] == item2[1]):
                x = True
            elif (abs(item1[0] - item2[0]) == abs(item1[1] - item2[1])) and ((item1[1] != item2[1]) or (item1[0] != item2[0])):
                x = True
if x:
    print('YES')
else:
    print('NO')