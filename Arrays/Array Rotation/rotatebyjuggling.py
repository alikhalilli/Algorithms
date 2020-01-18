import time


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


"""
[1, 2 | 3, 4 | 5, 6]
[x, 2 | 1, 4 | 5, 6]
[x, 2 | 5, 4 | 1, 6]
"""


"""
[1, 2, 3, 4, 5]
[4, 5, 1, 2, 3]
"""


def rotateLeft(arr, d):
    n = len(arr)
    k = d % n
    temp = [None]*k
    for i in range(k):
        temp[i] = arr[i]

    for i in range(n-k):
        arr[i] = arr[i+k]

    for i in range(k):
        arr[n-k+i] = temp[i]
    return arr


def rotateRight(arr, d):
    n = len(arr)
    k = d % n
    temp = [None] * k

    for i in range(k):
        temp[i] = arr[n-k+i]

    for i in range(n, k, -1):
        arr[i-1] = arr[i-k-1]

    for i in range(k):
        arr[i] = temp[i]

    return arr


def leftRotate(arr, d):
    n = len(arr)
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
        print("hmm")
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = (j + d) % n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
            print(arr)
        arr[j] = temp
        print(f"->{arr}")
    print(arr)


leftRotate([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
