"""
@github: github.com/alikhalilli

Time Complexity: O(n)
Space Complexity: O(n)
"""


def getPairs(arr1, arr2, sum):
    s = set()
    pairs = []
    for i in range(len(arr1)):
        s.add(arr1[i])
    for i in range(len(arr2)):
        if sum - arr2[i] in s:
            pairs.append((arr2[i], sum - arr2[i]))
    return pairs
 