def find_longest_zero_subarray(arr):
    s = 0
    maxx = 0
    for i in arr:
        if i == 0:
            s += 1
            if (s>maxx):
                maxx = s
        else:
            s = 0
    return maxx

def find_longest_zero_subarray2(arr):
    from itertools import groupby
    return max([len(list(g)) for k, g in groupby(coupe_count[1:]) if k != 0])


def main(seats):
    seat_map = [None]
    for i in range(1, 10):
        seat_map += [i] * 4
    for i in range(9, 0, -1):
        seat_map += [i] * 2

    coupe_count = [None] + [6] * 9

    for r in seats:
        coupe_count[seat_map[r]] -= 1

    return coupe_count

# M = find_longest_zero_subarray([1,1,1,1,0,0,0,0,0])

N = int(input())
seats = [int(input()) for i in range(N)]
coupe_count = main(seats)
M = find_longest_zero_subarray(coupe_count)