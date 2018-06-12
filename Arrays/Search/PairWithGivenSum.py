"""
@github: github.com/alikhalilli

arr = [4, 5, 6, 1, 2, 3]
"""


def findPivot(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[i + 1]:
            return i
    return -1


def findPair(arr, sum):
    n = len(arr)
    p = findPivot(arr)
    l = (p + 1) % n  # min element's index
    r = p  # max element's index
    while l != r:
        if arr[l] + arr[r] == sum:
            return (l, r)

        if (arr[l] + arr[r] < sum):
            l = (l + 1) % n
        else:
            r = (n + r - 1) % n
    return False
