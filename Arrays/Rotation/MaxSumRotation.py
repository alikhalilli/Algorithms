"""
@github: github.com/alikhalilli

Time Complexity: O(n^2)

arr = [1, 20, 2, 10]
Output: 72

{2, 10, 1, 20}
2*0 + 10*1 + 1*2 + 20*3 => 72
"""


def getMaxSUM(arr):
    n = len(arr)
    maxsum = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            k = (j + i) % n
            sum += j * arr[k]
            if sum > maxsum:
                maxsum = sum
    return maxsum


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(getMaxSUM(arr))
