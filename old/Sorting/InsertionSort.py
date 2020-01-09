"""
@github: github.com/alikhalilli

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
arr = [9, 8, 10, 5]


def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        static_point = arr[i]
        j = i-1
        while j >= 0 and arr[j] > static_point:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = static_point
    return arr


print(insertionSort(arr))
