A = input().split()
A = [int(i) for i in A]
s = 1
for i in range(len(A)-1):
    print(A[i], A[i+1])
    if (A[i] != A[i+1]):
        s += 1
print(s)
