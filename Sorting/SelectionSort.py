"""
@github: github.com/alikhalilli

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def swap(arr, i1, i2):
    temp = arr[i2]
    arr[i2] = arr[i1]
    arr[i1] = temp


def selectionSort(arr, asc=False):
    n = len(arr)
    for i in range(n):
        best_index = i
        for j in range(i, n):
            if asc:
                if arr[j] < arr[i]:
                    best_index = j
            else:
                if arr[j] > arr[i]:
                    best_index = j
        swap(arr, i, best_index)
    return arr


arr = [9, 8, 10, 5]
print(selectionSort(arr))
