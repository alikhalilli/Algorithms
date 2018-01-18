"""
@github: github.com/akhalilli

arr = [1, 2, 3, 4, 5]

d = 2
A = [1, 2]
rA = [2, 1]
B = [3, 4, 5]
rB = [5, 4, 3]

rArB = [2, 1, 5, 4, 3]
r(rArB) = [3, 4, 5, 1, 2]
"""

def rotateByReverse(arr, d):
	n = len(arr)
	reverseArray(arr, 0, d-1)
	reverseArray(arr, d, n-1)
	reverseArray(arr, 0, n-1)
	print(arr)


def reverseArray(arr, start, end):
	while start < end:
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp
		start += 1
		end = end - 1

arr = [1, 2, 3, 4, 5]
rotateByReverse(arr, 2)
