"""
@github: github.com/alikhalilli

Time Complexity: O(n^2)
Space Complexity: O(1)

Input : arr[] = {1, 2, 3, 4, 5, 6, 7}
                 0  1  2  3  4  5  6
           1   3   5
Output : 4 5 3 6 2 7 1
         0   2   4   6
Input : arr[] = {1, 2, 1, 4, 5, 6, 8, 8} 
Output : 4 5 2 6 1 8 1 8
"""


def swap(arr, e1, e2):
    temp = arr[e2]
    arr[e2] = arr[e1]
    arr[e1] = temp


"""
def rearrangeOddEven(arr):
    n = len(arr)
    for i in range(n):
        m = i % 2
        for j in range(n-m, m, -2):
            if m == 0:
                if arr[j-1] > arr[j-3]:
                    swap(arr, j-1, j-3)
            elif m == 1:
                if arr[j-1] < arr[j-3]:
                    swap(arr, j-1, j-3)
    return arr
"""


def rearrangeOddEven(arr):
    n = len(arr)
    for i in range(n):
        m = i % 2
        for j in range(m, n-m, 2):
            if m == 0:
                if arr[i] > arr[j]:
                    swap(arr, i, j)
            else:
                if arr[i] < arr[j]:
                    swap(arr, i, j)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
# arr = [1, 1, 2, 4, 5, 6, 8, 8]
print(rearrangeOddEven(arr))
