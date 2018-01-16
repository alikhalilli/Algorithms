"""
Time Complexity: O(n*d)
Auxiliary Space: O(1)
"""


def rotateArray(arr, d, left=True):
    n = len(arr)
    if left:
        leftRotate(arr, d, n)
    else:
        rightRotate(arr, d, n)


def leftRotate(arr, d, n):
    for i in range(d):
        leftRotateByOne(arr, n)
    print("Left Rotated: ", arr)


def rightRotate(arr, d, n):
    for i in range(d):
        rightRotateByOne(arr, n)
    print("Right Rotated: ", arr)


def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def rightRotateByOne(arr, n):
    temp = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = temp


a = [1, 2, 3, 4, 5, 6, 7]
rotateArray(a, 2, False)
