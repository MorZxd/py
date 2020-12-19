N = int(input())
S = 0
badIdx = -1
is_start_equal = True
start_number = -1
for i in range(N):
    a = int(input())

    if is_start_equal:
        if start_number == -1:
            start_number = a
        if a != start_number:
            is_start_equal = False
        else:
            badIdx = i
      
    if (not is_start_equal) and (a >= S):
        badIdx = i-1
    S += a

if N == 1:
    print('1')
else:
    for i in range(N):
        if (i>badIdx):
            print('1')
        else:
            print('0')
        
