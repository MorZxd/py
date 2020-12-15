import math

def power_rec(a,n):
    if n == 0:
        return 1
    else:
        return a*power(a, n-1)


def power_simple(a,n):
    res = 1
    for i in range(n):
        res = a*res
    return res

def power_2less(a,n):
    return power_simple(a*a, n//2) * power_simple(a,n%2)

def power_4less(a, n):
    return power_simple(power_simple(a,4), n//4) * power_simple(a,n%4)

def power_8less(a, n):
    return power_simple(power_simple(a,8), n//8) * power_simple(a,n%8)


def power_optimium(a, n):
    k = math.sqrt(n) // 1
    return power_simple(power_simple(a,k), n//k) * power_simple(a,n%k)


def to_base2(n):
    # return [0,0,1,0,0,1,1,1,1,1,1]
    return [0,1,0,1]

def power_superoptimal(a,n):
    base2 = to_base2(n)
    res = a
    summ = 1
    for i in base2:
        if i != 0:
            summ = summ * res
        res = res * res
    return summ



# 2020 = 2**10 + 2**9 + 2**8 + 2**7 + 2**6 + 2**5 + 2**2 = 11111100100(2)

# 7**2020 = 7**(2**10 + 2**9 + 2**8 + 2**7 + 2**6 + 2**5 + 2**2) = 7**(2**2) * 7**(2**5) * 7**(2**6) * ....

# - 7**2
# - (7**2)**2 = 7 ** (2**2)
# - (7 ** (2**2))**2 = 7 ** (2**3)
# - (7**(2**3))**2 = 7**(2**4)
# - ...
# - 7**(2**10)
# - ...
# - 7**(2**20)

def power_kless(a, n, k):
    # k - 1 + n / k - 1
    # k + n / k >= 2 sqrt(n)

    # (a + b)/2 >= sqrt(ab)
    # a + b >= 2sqrt(ab)
    # a - 2sqrt(ab) + b >= 0
    # (sqrt(a) - sqrt(b))**2 >= 0

    # k = n / k
    # k = sqrt(n)
    return power_simple(power_simple(a,k), n//k) * power_simple(a,n%k)


def power_less(a, n):
    #скорее всего метод отличающийся от методов выше, т.к. если делать тоже самое при этом брать максимальный порог получится power_simple(power_simple(a,n),1)?
    return power_simple(a)

assert power_simple(5, 1) == 5
assert power_simple(5, 0) == 1

assert power_8less(2, 10) == 2 ** 10
print(power_8less(2, 10))

assert power_superoptimal(2, 10) == 2**10