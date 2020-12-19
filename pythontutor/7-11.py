A = input().split()
A = [int(i) for i in A]
for i in range(k+1, len(A)):
    A[i-1] = A[i]
A.pop()
print(A)