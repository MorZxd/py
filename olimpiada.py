konf = 2020
deti = [0] * 67
i = 1
otv = 0
skip = 0
while (konf != 0):
    deti[(i+skip)%67] += 1
    konf -= 1
    i +=1
    skip += 1
for i in deti:
    if (i == 0):
        otv += 1
print(otv)
