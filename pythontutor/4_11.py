N = int(input())
summ = (N * (N + 1)) // 2
for i in range(N - 1):
    a = int(input())
    summ -= a
print(summ)