"""
@github: github.com/alikhalilli

Time Complexity: O(logn)
Space Complexity: O(1)
"""


def findMinElement(arr, low, high):
    if low > high:
        return -1
    if low == high:
        return low

    mid = int(low + (high - low)/2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return arr[mid + 1]

    if low < mid and arr[mid] < arr[mid - 1]:
        return arr[mid]

    if arr[low] >= arr[mid]:
        return findMinElement(arr, low, mid-1)

    return findMinElement(arr, mid+1, high)
