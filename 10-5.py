from copy import deepcopy

n, m = [int(item) for item in input().split()]
arr = [[int(item) for item in input().split()] for _ in range(n)]
i, j = [int(item) for item in input().split()]
def swap_columns(arr0, i, j):
    arr = deepcopy(arr0)
    for row in arr:
    # x = arr[idx][j]
    # arr[idx][j] = arr[idx][i]
    # arr[idx][i] = x
        row[j], row[i] = row[i], row[j]
    return arr

arr1 = swap_columns(arr, i, j)

def show(arr):
    for row in arr:
        rowS = [str(item) for item in row]
        print(' '.join(rowS))

show(arr)