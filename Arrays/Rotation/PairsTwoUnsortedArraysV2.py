"""
@github: github.com/alikhalilli

Time Complexity: O(n)
Space Complexity: O(n)
"""


def findPair(arr1, arr2, sum):
    s = set()
    for i in range(len(arr1)):
        s.add(arr1[i])
    for i in range(len(arr2)):
        if sum - arr2[i] in s:
            return (arr2[i], sum - arr2[i])
