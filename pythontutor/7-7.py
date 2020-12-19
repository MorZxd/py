A = input().split()
A = [int(i) for i in A]
x = int(input())
# s = 0
# for item in A:
#     s += 1
#     if (item<x):
#         break
s = 0
while A[s] >= x:
    s += 1
print()