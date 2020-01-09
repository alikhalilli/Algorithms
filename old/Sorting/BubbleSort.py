"""
@github: github.com/alikhalilli

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def bubbleSort(arr, asc=True):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(n-i-1):
            if asc:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            else:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
        if swapped == False:
            break
    return arr


arr = [9, 8, 10, 5, -1, 20]
print(bubbleSort(arr, False))
