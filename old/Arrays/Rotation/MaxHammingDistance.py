"""
@github: github.com/alikhalilli

Time Complexity: 
Space Complexity: 

[1, 2, 3, 4, 5]
[2, 3, 4, 5, 1]
[3, 4, 5, 1, 2]
[4, 5, 1, 2, 3]
[5, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
"""


def getMaxHammingDistance(arr):
    n = len(arr)
    maxDistance = 0
    for i in range(1, n):
        currDistance = 0
        k = 0
        for j in range(i, i+n):
            if arr[j % n] != arr[k]:
                currDistance += 1
            k += 1
        maxDistance = max(maxDistance, currDistance)
    return maxDistance


arr = [2, 2, 2, 1]
print(getMaxHammingDistance(arr))
