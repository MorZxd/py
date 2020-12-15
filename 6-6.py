n = int(input())
compare = False
s = 0
while n != 0:
    if compare:
        if n>m:
            s = s+1
    m = n
    compare = True
    n = int(input())
print(s)
