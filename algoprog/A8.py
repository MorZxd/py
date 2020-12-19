n = int(input())
S = 0
while (n > 0):
    S += n%10
    n = n//10
print(S)