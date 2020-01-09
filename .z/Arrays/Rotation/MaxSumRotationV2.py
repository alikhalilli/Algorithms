"""
@github: github.com/alikhalilli

Time Complexity: O(n)
Space Complexity: O(1)

arr = [1, 20, 2, 10]
Output: 72

{2, 10, 1, 20}
2*0 + 10*1 + 1*2 + 20*3 => 72
"""

"""
R0 = 0*arr[0] + 1*arr[1] +...+ (n-1)*arr[n-1]
R1 = 0*arr[n-1] + 1*arr[0] +...+ (n-1)*arr[n-2]
R2 = 0*arr[n-2] + 1*arr[n-1] +...+ (n?1)*arr[n-3]

R1 - R0 = arr[0] + arr[1] + ... + arr[n-2] - (n-1)*arr[n-1]
R2 - R1 = arr[0] + arr[1] + ... + arr[n-3] - (n-1)*arr[n-2] + arr[n-1]

Rj - Rj-1 = arrSum - n * arr[n-j]

Where arrSum is sum of all array elements, i.e., 
arrSum = ∑ arr[i]
        i <= 0 <= n-1 
"""


def getMaxSum(arr):
    n = len(arr)
    arrsum = 0
    maxsum = 0
    currval = 0
    for i in range(n):
        arrsum += arr[i]
        currval += i*arr[i]

    for j in range(1, n):
        currval += arrsum - n * arr[n-j]
        if maxsum < currval:
            maxsum = currval
    return maxsum


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(getMaxSum(arr))
