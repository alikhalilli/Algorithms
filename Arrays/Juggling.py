"""
@github: github.com/akhalilli

Time Complexity: O(n)
Space Complexity: O(1)
"""

def leftRotate(arr, d, n):
    for i in range(gcd(d, n)):
        temp = arr[i]
        j = i
        while 1:
            k = (j + d) % n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

"""

1 2 3 4 5 6 7 8 9 10 11 12
n = 12
d = 3
gcd = 3
[1 2 3] [4 5 6] [7 8 9] [10 11 12]

arr[0] - arr[3] - arr[6] - arr[9] - (9+3)%12

[4 2 3] [7 5 6] [10 8 9] [1 11 12]

[4 5 3] [7 8 6] [10 11 9] [1 2 12]

[4 5 6] [7 8 9] [10 11 12] [1 2 3]
"""

# GCD = Greatest Common Divisor
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
