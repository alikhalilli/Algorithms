"""
@github: github.com/alikhalilli

arr = [5, 6, 1, 2, 3, 4]

Time Complexity: O(logn)
Space Complexity: O(1)
"""


def findPivotIndex(arr, low, high):
    if low > high:
        return -1
    if low == high:
        return low

    mid = int(low + (high - low)/2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid

    if low < mid and arr[mid] < arr[mid - 1]:
        return mid-1

    if arr[low] >= arr[mid]:
        return findPivotIndex(arr, low, mid-1)

    return findPivotIndex(arr, mid+1, high)


def getRotationCount(arr):
    n = len(arr)
    p = findPivotIndex(arr, 0, n-1)
    return p % n
