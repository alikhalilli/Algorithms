"""
@github: github.com/alikhalilli

Input : arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

Input : arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
"""


def rearrange(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] != i or arr[i] != -1:
            for j in range(n):
                if i != j and arr[j] == i:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    break
    print(arr)


def rearrangeV2(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] != i and arr[i] != -1:
            x = arr[i]
            while (arr[x] != -1 and arr[x] != x):
                y = arr[x]
                arr[x] = x
                x = y
            arr[x] = x
            if arr[i] != i:
                arr[i] = -1


arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
rearrange(arr)
