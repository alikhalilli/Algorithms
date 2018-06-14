"""
@github: github.com/alikhalilli

Time Complexity: O(n)

[1, 2, 3, 4]
[4, 3, 2, 1]
"""


def reverseArr(arr):
    n = len(arr)
    l = 0
    r = n-1
    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l += 1
        r -= 1
    print(arr)


arr = [1, 2, 3, 4, 0]
reverseArr(arr)
