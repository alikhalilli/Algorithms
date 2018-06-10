
"""
@github: github.com/alikhalilli

Time Complexity: O(n * d) # d times OneByOne()
Auxiliary Space: O(1) # temp = arr[0] or arr[-1]
"""


class Solution(object):

    def __init__(self, arr, direction, d, printarr=True):
        self.arr = arr
        self.direction = direction
        self.n = len(arr)
        self.d = d % self.n
        self.print = printarr

    def rotate(self):
        for i in range(self.d):
            if self.direction == 'left':
                temp = self.arr[0]
                self.__leftRotate()
                self.arr[-1] = temp
            if self.direction == 'right':
                temp = self.arr[-1]
                self.__rightRotate()
                self.arr[0] = temp

        if self.print:
            print(self.arr)

    def __leftRotate(self):
        """
        [1, 2, 3, 4, 5]
        [2, 3, 4, 5, 5]
        """
        for i in range(self.n-1):
            self.arr[i] = self.arr[i+1]

    def __rightRotate(self):
        """
        [1, 2, 3, 4, 5]
        [1, 1, 2, 3, 4]
        """
        for i in range(self.n-1, 0, -1):
            self.arr[i] = self.arr[i - 1]


arr = [1, 2, 3, 4, 5]
sol = Solution(arr, 'right', -2)
sol.rotate()
