n = int(input())
words = set()
for i in range(n):
    words |= set(input().split())
res = len(words)
print(res)