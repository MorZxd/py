mx = int(input())
august_number = int(input())
august_number = str(august_number)
res = set([str(i) for i in range(1, mx+1)])
while True:
    inp = input()
    if inp == 'HELP':
        # break
        print(" ".join(res))
        continue
    query = set(inp.split())
    

    # inp = input()
    august_answer = (august_number in query) 
    # if (inp == "YES"):
    if august_answer:
        res = res & query
    # elif (inp == "NO"):
    else:
        res = res - query
    print('YES' if august_number in query else 'NO')
