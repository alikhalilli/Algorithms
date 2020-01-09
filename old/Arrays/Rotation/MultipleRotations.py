"""
@github: github.com/alikhalilli

Time Complexity: O(n)
Space Complexity: O(2n)

arr = [1, 2, 3, 4, 5, 6]
k1 = 1, [2, 3, 4, 5, 6, 1]
k2 = 3, [4, 5, 6, 1, 2, 3]
k3 = 4, [5, 6, 1, 2, 3, 4]
"""


def fillTemp(arr):
    n = len(arr)
    temp = [None]*(2*n)
    for i in range(n):
        temp[i] = temp[i+n] = arr[i]
    return temp


def leftRotate(arr, k):
    n = len(arr)
    temp = fillTemp(arr)
    start = k % n
    for i in range(start, start+n):
        print(temp[i], end=" ")
