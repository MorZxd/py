a = [int(i) for i in input().split()]
x = 0
m = a[0]

for i, item in enumerate(a):
    if (item > m):
        m = item
        x = i
print(m, x)
# for x in enumerate(a):
    # i = x[0]
    # item = x[1]
    # print(i, item)

# for i in range(len(a)):
    # if (a[i]>a[x]):
#         x = i
# print(a[x], x)