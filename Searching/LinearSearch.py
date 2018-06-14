"""
@github: github.com/alikhalilli
"""


def linearSearch(arr, key):
    n = len(arr)
    result = False
    for i in range(n):
        if arr[i] == key:
            result = i
            break
    return result


arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
print(linearSearch(arr, 30))
