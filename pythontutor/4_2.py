a = int(input())    
b = int(input())

if (a>b):
    M = b-1
    m = a
    step = -1
else:
    m = a
    M = b+1
    step = 1


for i in range(m, M, step):
    print(i, sep = " ", end = " ")
 
