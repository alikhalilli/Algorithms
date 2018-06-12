"""
@github: github.com/alikhalilli

arr = [1, 4, 45, 6, 10, -8]
pair_sum = 16
init l=0, r=5

1. Sort the array in non-decreasing order.
2. Initialize two index variables to find the candidate
elements in the sorted array.
    a) Init first to the leftmost index, l=0
    b) Init second to the rightmost index, r=arr_size-1
3. Loop while l < r.
    a) if (A[l] + A[r] == sum) then return 1
    b) else if (A[l] + A[r] < sum) then l++
    c) else r--
4. No candidates on whole array, return 0
"""


def findPair(arr, sum):
    n = len(arr)
    l = 0
    r = n - 1
    while l < r:
        if arr[l] + arr[r] == sum:
            return (l, r)
        elif arr[l] + arr[r] < sum:
            l += 1
        else:
            r -= 1
    return 0


# arr = [1, 4, 45, 6, 10, -8]
arr = [-8, 1, 4, 6, 10, 45]
print(findPair(arr, 16))
