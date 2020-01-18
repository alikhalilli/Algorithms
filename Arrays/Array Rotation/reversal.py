arr = [1, 2, 3, 4, 5, 6]


def rotateLeft(arr, d):
    n = len(arr)
    d = d % n
    reverseArr(arr, 0, d-1)
    reverseArr(arr, d, n-1)
    reverseArr(arr, 0, n-1)
    print(arr)


def reverseArr(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


rotateLeft(arr, 2)
