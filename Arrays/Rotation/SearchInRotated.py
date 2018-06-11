"""
@github: github.com/alikhalilli

Time Complexity: O(logn)
"""


def binarySearch(arr, low, high, key):
    if high < low:
        return -1

    mid = int(low + (high - low) // 2)

    if arr[mid] == key:
        return mid

    if arr[mid] > key:
        return binarySearch(arr, low, mid-1, key)

    if arr[mid] < key:
        return binarySearch(arr, mid+1, high, key)


def findPivotIndex(arr, low, high):
    if high < low:
        return -1

    if high == low:
        return low

    mid = int(low + (high - low) / 2)

    if mid < high and arr[mid] > arr[mid+1]:
        return mid

    if mid > low and arr[mid] < arr[mid-1]:
        return mid-1

    """
    [1, 2, 3, 4, 5, 6]
    [3, 4, 5, 6, 1, 2]
    arr[0] >= arr[3]
    """
    if arr[low] >= arr[mid]:
        return findPivotIndex(arr, low, mid-1)

    return findPivotIndex(arr, mid+1, high)


def pivotedSearch(arr, key):
    n = len(arr)
    pivot = findPivotIndex(arr, 0, n-1)

    if pivot == -1:
        return binarySearch(arr, 0, n-1, key)  # normal Binary-Search

    if arr[pivot] == key:
        return pivot

    if arr[0] <= key:
        return binarySearch(arr, 0, pivot-1, key)

    return binarySearch(arr, pivot+1, n-1, key)
