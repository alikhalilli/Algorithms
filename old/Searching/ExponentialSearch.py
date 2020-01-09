"""
@github: github.com/alikhalilli

Time Complexity: O(logn)
Space Complexity: O(1)
"""


def binarySearch(arr, key, l, h):
    while l <= h:
        mid = int(l + (h - l)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            h = mid - 1
        elif arr[mid] < key:
            l = mid + 1
    return False


def exponentialSearch(arr, key):
    n = len(arr)
    if arr[0] == key:
        return 0
    i = 1
    while i < n and arr[i] < key:
        prev = i
        i *= 2
    return binarySearch(arr, key, prev, min(i, n))
