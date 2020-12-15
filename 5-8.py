s = input()
hl = s.find('h')
hr = s.rfind('h')
print(s[:hl]+s[hr:hl:-1]+s[hr:])