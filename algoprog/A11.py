a1, a2, a3 = int(input()), int(input()), int(input())
b1, b2, b3 = int(input()), int(input()), int(input())
ar = a1*60*60+a2*60+a3
br = b1*60*60+b2*60+b3
print(abs(ar-br))