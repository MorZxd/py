N = int(input())

fin = [0] * (N + 1)

for i in range(1, N + 1):
    x = i
    y = int(input())
    xx = N + 1 - y
    yy = x
    fin[xx] = yy

print('-----')

for i in fin[1:]:
    print(i)