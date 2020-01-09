"""
@github: github.com/alikhalilli

Time Complexity: O(n)

1. Init an empty hash table s (set).
2. Do following for each element A[i] in A:
    a) If s[x - A[i]] is set then print the pair (A[i], x - A[i])
    b) Insert A[i] into s.
"""


def findPair(arr, sum):
    n = len(arr)
    s = set()
    """
    temp = sum - arr[i]
    sum - arr[i] = old_x
    sum = arr[i] + old_x
    return (arr[i], old_x)
    """
    for i in range(n):
        temp = sum - arr[i]
        if temp >= 0 and temp in s:
            return (arr[i], temp)
        s.add(arr[i])
