"""
@github: github.com/alikhalilli

arr = [5, 6, 1, 2, 3, 4]

Time Complexity: O(n)
Space Complexity: O(1)
"""


def getCount(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        count += 1
        if arr[i] > arr[(i+1) % n]:
            break
    return count % n


arr = [3, 4, 5, 6, 1, 2]
print(getCount(arr))
