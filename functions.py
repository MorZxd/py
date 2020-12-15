# def f(n):
#     n = n + 1
#     return n

# k = 1
# m = f(k)

# print(k)

############################

# def g(arr):
#     # arr.append(1)
#     arr = arr + [1]
#     return arr

# aaa = [1,2,5]
# bbb = g(aaa)

# print(aaa)


############################

def intdivide(a, b):
    return a // b, a % b

a = 90
b = 8

k, m  = intdivide(a, b)

print(k, m)
