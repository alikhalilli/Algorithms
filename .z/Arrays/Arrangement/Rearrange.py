"""
@github: github.com/alikhalilli

Input : arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

Input : arr = [19, 7, 0, 3, 18, 15, 12, 6,
    1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
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
            k = 0
            for j in range(n):
                k += 1
                if arr[j] == i:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    break
            print(k)
            if k == n-1:
                arr[i] = -1
        print(arr)


arr = [19, 7, 0, 3, 99, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]

# rearrangeV2(arr)

# arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]


def rearrangeV3(arr):
    n = len(arr)
    d = set()
    for i in range(n):
        d.add(arr[i])
    print(d)
    for i in range(n):
        if i in d:
            arr[i] = i
        else:
            arr[i] = -1
    print(arr)


def rearrangeV4(arr):
    n = len(arr)
    d = {}
    for i in range(n):
        d[arr[i]] = i
    print(d)
    for i in range(n):
        if i in d.keys():
            arr[i] = i
        else:
            arr[i] = -1
    print(arr)


rearrangeV4(arr)


def rearrangeArr(arr):
    n = len(arr)
    s = set()
    for i in range(n):
        s.add(arr[i])
    for i in range(n):
        if i in s:
            arr[i] = i
        else:
            arr[i] = -1


def rearrangeV6(arr):
    n = len(arr)
    for i in range(0, n):
        if (arr[i] != -1 and arr[i] != i):
            x = arr[i]
            while (arr[x] != -1 and arr[x] != x):
                y = arr[x]
                arr[x] = x
                x = y
            arr[x] = x

            if (arr[i] != i):
                arr[i] = -1
    return arr


arr = [19, 7, 0, 3, 99, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
print(rearrangeV6(arr))
