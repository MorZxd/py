n = int(input())
d = {}
for i in range(n):
    s = input()
    words = s.split()
    for word in words:
        d[word] = d.get(word, 0) + 1 
L = [(-val, key) for key, val in d.items()]
L.sort()
for _, word in L:
    print(word)