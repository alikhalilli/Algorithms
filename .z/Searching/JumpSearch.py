"""
@github: github.com/alikhalilli

Time Complexity: O(sqrt(n))
Space Comlexity: O(1)

[1, 2, 3, 4, 5, 6]
b_size=2
 0  1   2   3  4  5
[1, 2, -3-, 4, 5, 6]
[1, 2, 3, 4, -5-, 6]

"""
from math import sqrt, floor


def jumpSearch(arr, key):
    n = len(arr)
    b_size = int(sqrt(n))
    l = 0
    prev = 0
    while arr[l] <= key:
        if l + b_size >= n-1:
            l = n-1
            break
        else:
            prev = l
            l = l + b_size

    for i in range(l, prev-1, -1):
        if arr[i] == key:
            return i
    return False


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print(jumpSearch(arr, 0))
