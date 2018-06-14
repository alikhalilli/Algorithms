"""
@github: github.com/alikhalilli

Time Complexity: O(n)

[1, 2, 3, 4]
[4, 3, 2, 1]
"""


def reverseArr(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverseArr(arr, l+1, r-1)


arr = [1, 2, 3, 4, 0]
l = 0
r = len(arr) - 1
reverseArr(arr, l, r)
