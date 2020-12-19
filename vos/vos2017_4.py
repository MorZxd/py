seat_map = [None] * 55
for i in range(1, 37):
    seat_map[i] = (i-1) // 4 + 1
for i in range(37, 55):
    seat_map[i] = (54 - i) // 2 + 1
coupe_count = [None] * 10
for i in range(1,10):
    coupe_count[i] = 6
N = int(input())
for i in range(N):
    r = int(input())
    coupe_count[seat_map[r]] -= 1

s = 0
maxx = 0
for i in coupe_count[1:]:
    if i == 0:
        s += 1
        if (s>maxx):
            maxx = s
    else:
        s = 0
print(maxx)