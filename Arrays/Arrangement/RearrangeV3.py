"""
@github: github.com/alikhalilli

Time Complexity: O(n)
Space Complexity: O(n)
"""


def rearrangeArr(arr):
    n = len(arr)
    d = dict()
    for i in range(n):
        d[arr[i]] = i
    for i in range(n):
        if i in d.keys():
            arr[i] = i
        else:
            arr[i] = -1
    return arr


arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(rearrangeArr(arr))
