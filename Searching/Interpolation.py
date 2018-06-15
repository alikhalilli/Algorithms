"""
@github: github.com/alikhalilli

Time Complexity: best: O(loglogn), worst: O(n)
Space Comlexity: O(1)
"""


def interpolationSearch(arr, key):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        pos = low + \
            int(float((key - arr[low])*(high-low) / (arr[high] - arr[low])))
        if arr[pos] == key:
            return pos
        elif arr[pos] > key:
            high = pos - 1
        elif arr[pos] < key:
            low = pos + 1
    return False


arr = [1, 2, 3, 4, 5, 6, 70, 80]
print(interpolationSearch(arr, 6))
