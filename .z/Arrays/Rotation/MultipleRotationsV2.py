"""
@github: github.com/alikhalilli

Time Complexity: O(n)
Space Complexity: O(1)

arr = [1, 2, 3, 4, 5, 6]
k1 = 1, [2, 3, 4, 5, 6, 1]
k2 = 3, [4, 5, 6, 1, 2, 3]
k3 = 4, [5, 6, 1, 2, 3, 4]
"""


def leftRotate(arr, k):
    n = len(arr)
    start = k % n
    for i in range(start, start+n):
        print(arr[i % n], end=" ")


def rightRotate(arr, k):
    n = len(arr)
    start = (n-k) % n
    for i in range(start, start+n):
        print(arr[i % n], end=" ")


leftRotate([1, 2, 3, 4, 5, 6], 2)
