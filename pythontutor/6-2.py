n = int(input())
if (n%2 == 0):
    print(2)
else:
    i = 3
    while n % i != 0:
        i = i+1
    print(i)