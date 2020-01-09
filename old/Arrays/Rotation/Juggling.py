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

1 2 3 4 5 6 7 8 9 10 11 12
n = 12
d = 3
gcd = 3
[1 2 3] [4 5 6] [7 8 9] [10 11 12]

arr[0] - arr[3] - arr[6] - arr[9] - (9+3)%12

[4 2 3] [7 5 6] [10 8 9] [1 11 12]

[4 5 3] [7 8 6] [10 11 9] [1 2 12]

[4 5 6] [7 8 9] [10 11 12] [1 2 3]

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution(object):
    def __init__(self, arr, d, printarr=True):
        self.arr = arr
        self.n = len(arr)
        self.d = d % self.n
        self.gcd = self.__getGCD(self.n, self.d)
        self.print = printarr

    def rotate(self):
        for i in range(self.gcd):
            temp = self.arr[i]
            j = i
            while True:
                k = (j + self.d) % self.n
                if k == i:
                    break
                self.arr[j] = self.arr[k]
                j = k
            self.arr[j] = temp

        if self.print:
            print(self.arr)

    def __getGCD(self, a, b):
        """
        a=12, b=3
        if a%b==0: return b
        """
        if b == 0:
            return a
        else:
            return self.__getGCD(b, a % b)


arr = [1, 2, 3, 4, 5]
sol = Solution(arr, 2)
sol.rotate()
