"""
@github: github.com/alikhalilli

Time Complexity: O(logn)
"""


def binarySearch(arr, low, high, key):
    if low > high:
        return False
    mid = int(low + (high - low) / 2)

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, low, mid-1, key)
    elif arr[mid] < key:
        return binarySearch(arr, mid+1, high, key)


arr = [1, 2, 3, 4, 5, 6, 70, 80]
print(binarySearch(arr, 0, len(arr)-1, 70))
