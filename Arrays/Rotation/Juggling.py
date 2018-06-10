"""
@github: github.com/alikhalilli
Instead of moving one by one,
divide the array in different sets
where number of sets is equal to GCD
of n and d and move the elements
within sets.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = 12, d=3
GCD = Greatest Common Divisor
GCD(12, 3) = 3

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temp = arr[0] = 1
j = 0
k = j + 2 => 2
[10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution(object):
    def __init__(self, arr, d):
        self.arr = arr
        self.n = len(arr)
        self.d = d % self.n
        self.gcd = self.__getGCD(n, d)

    def rotate(self):
        for i in range(self.gcd):
            temp = self.arr[i]
            j = i
            while True:
                k = j + self.d
                if k >= self.n:
                    k = k % self.n
                if k == i:
                    break
                self.arr[j] = self.arr[k]
                j = k
            self.arr[j] = temp

    def __getGCD(self, a, b):
        """
        a=12, b=3
        if a%b==0: return b
        """
        if b == 0:
            return a
        else:
            return self.__getGCD(b, a % b)
