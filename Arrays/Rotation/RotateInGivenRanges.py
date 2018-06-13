"""
@github: github.com/alikhalilli

arr = [1, 2, 3, 4, 5]
r_indexes = (0, 2)
l, r = 0, 2
n_r = 2
"""
ranges = [(0, 2), (0, 3)]
arr = [1, 2, 3, 4, 5]


def leftRotate(arr, r_indexes):
    l, r = r_indexes
    n = len(arr)
    n_r = r - l
    temp = arr[n_r]
    for i in range(n_r, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp


def rotateWithRange(arr, ranges):
    for r_indexes in ranges:
        leftRotate(arr, r_indexes)
    return arr


print(rotateWithRange(arr, ranges))
