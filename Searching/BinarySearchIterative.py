"""
@github: github.com/alikhalilli

Time Complexity: O(logn)
"""


def binarySearch(arr, key):
    low = 0
    high = len(arr)-1
    while (low <= high):
        mid = int(low + (high-low)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return False


arr = [1, 2, 3, 4, 5, 6, 70, 80]
print(binarySearch(arr, 1))
