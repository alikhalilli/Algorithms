"""
@github: github.com/alikhalilli

arr = [9, 8, 10, 3, 5]

Time Complexity: O(n^2)
Space Complexity: O(n) (function callstack)
"""


def bubbleSort(arr, c_index):
    #print((len(arr)-c_index-1)*" ", "c=", c_index)
    if c_index == 0:
        return
    bubbleSort(arr, c_index-1)
    j = len(arr) - c_index - 1
    #print((j+1)*" ", "j=", j)
    while j < len(arr)-1:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        j += 1


#arr = [4, 7, 3, 5, 1]
arr = [1, 2, 3, 4, 5, 6, 7]
bubbleSort(arr, len(arr)-1)
print(arr)
