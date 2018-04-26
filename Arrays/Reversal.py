"""
@github: github.com/akhalilli

arr = [1, 2, 3, 4, 5]

d = 2
A = [1, 2]
rA = [2, 1]
B = [3, 4, 5]
rB = [5, 4, 3]

rArB = [2, 1, 5, 4, 3]
r(rArB) = [3, 4, 5, 1, 2]
"""

arr = [1, 2, 3, 4, 5]

rotate(arr, 2)


def rotate(arr, d):
    n = len(arr)
    d = d % n
    if n > 0:
        reverse(arr, 0, d-1)
        reverse(arr, d, n-1)
        reverse(arr, 0, n-1)


def reverse(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1
