"""
@github: github.com/alikhalilli

Time Complexity:
Space Complexity:
"""


def partition(arr, l, h):
    mi = l - 1
    pi = arr[h]
    for i in range(l, h):
        if arr[i] <= pi:
            mi += 1
            arr[mi], arr[i] = arr[i], arr[mi]
    arr[mi+1], arr[h] = arr[h], arr[mi+1]
    print(arr)
    return mi+1


def quickSort(arr, l, h):
    if l < h:
        pi = partition(arr, l, h)
        quickSort(arr, l, pi-1)
        quickSort(arr, pi+1, h)


arr = [4, 5, 3, 2, 6]
quickSort(arr, 0, len(arr)-1)
# print(arr)
