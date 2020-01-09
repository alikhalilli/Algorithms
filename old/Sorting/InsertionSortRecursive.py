"""
@github: github.com/alikhalilli

Time Complexity: O(n)
Space Complexity: O(n) (function callstack)
"""
arr = [9, 8, 10, 5]


def insertionSort(arr, n):
    if n <= 1:
        return
    insertionSort(arr, n-1)
    static_point = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > static_point:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = static_point


insertionSort(arr, len(arr))
print(arr)
