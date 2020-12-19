d={}
for i in range(int(input())):
  s = input().split()
  d[s[0]] = [s[i] for i in range(1, len(s))]
for i in range(int(input())):
  town = input()
  for i in d:
    if town in d[i]:
      print(i)
