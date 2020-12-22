n = int(input())
s = "a"
for i in range(n):
    if (int(input()) == 0):
        s = "YES"
        break
    else:
        s = "NO"
print(s)