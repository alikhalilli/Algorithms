"""
@github: github.com/alikhalilli

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def findPair(arr1, arr2, sum):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] + arr2[j] == sum:
                return (i, j)
    return -1
