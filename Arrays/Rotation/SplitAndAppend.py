"""
@github: github.com/alikhalilli

Time Complexity:
Space Complexity:
"""


def splitArrAppend(arr, k):
    n = len(arr)
    for i in range(k):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    return arr


arr = [1, 2, 3, 4, 5]
print(splitArrAppend(arr, 2))
