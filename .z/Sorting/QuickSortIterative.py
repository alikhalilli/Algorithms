"""
@github: github.com/alikhalilli
"""


def partition(arr, l, h):
    i = l-1
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return -1


def quickSort(arr, l, h):
    n = len(arr)
    stack = [None]*n
    top = -1
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr, l, h)

        if p-1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p-1
        if p-1 < h:
            top += 1
            stack[top] = p+1
            top += 1
            stack[top] = h
