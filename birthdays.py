days = 365
pupils = 24
otv = 1
for i in range(pupils):
    otv *= (days-i)/days
print(otv)