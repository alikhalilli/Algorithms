
"""
@github: github.com/akhalilli

Time Complexity: O(n)
Auxiliary Space: O(d)
"""


def rotateArray(arr, d, left=True):
    n = len(a)
    if left:
        print(leftRotate(arr, d, n))
    else:
        print(rightRotate(arr, d, n))


def leftRotate(arr, d, n):
    temp = []
    for i in range(n - d, n):
        temp.append(arr[i])

    for i in range(n, d, -1):
        arr[i - 1] = arr[i - d - 1]

    for i in range(d):
        arr[i] = temp[i]
    return arr


def rightRotate(arr, d, n):
    temp = []
    for i in range(d):
        temp.append(arr[i])

    for i in range(n - d):
        arr[i] = arr[i + d]

    for i in range(d):
        arr[n - d + i] = temp[i]
    return arr


a = [1, 2, 3, 4, 5, 6, 7]
rotateArray(a, 3, False)
