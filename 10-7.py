mx = int(input())
res = set([str(i) for i in range(1, mx+1)])
while True:
    inp = input()
    if inp == 'HELP':
        break
    query = set(inp.split())
    inp = input()
    if (inp == "YES"):
        res = res & query
    elif (inp == "NO"):
        res = res - query
print(" ".join(res))
