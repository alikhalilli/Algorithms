"""
@github: github.com/alikhalilli

Time Complexity: 
Space Compexity:

while s_size < n-1
while l < n-1

 0 1 2 3 4 5 6 7
|1|2|3|4|5|6|7|8| s_size=1
l1=0, l2=l1+s_size, l3=l2+s_size
l = [0, -, 2, -, 4, -, 6, -]
r = [-, 1, -, 3, -, 5, -, 7]


|1 2|3 4|5 6|7 8| s_size=2
l1=0, l2=l1+s_size=2, l3=l2+s_size=4, l4=l3+s_size=6
l = [0, -, 4, -]
r = [-, 3, -, 7]

 0 1 2 3 4 5 6 7
|1 2 3 4|5 6 7 8| s_size=4
l1=0, l2=l1+s_size=4
l = [0, 4]
r = [3, 7]

|1 2 3 4 5 6 7 8| s_size=8
l1=0
[0]
[7]
"""


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [None]*n1
    R = [None]*n2

    for i in range(n1):
        L[i] = arr[l+i]

    for i in range(n2):
        R[i] = arr[m+1+i]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr):
    n = len(arr)
    s_size = 2
    last = False
    while s_size <= n:
        l = 0
        if l + s_size < n:
            r = l + s_size - 1
        else:
            r = n-1
        while l < r:
            m = int(l + (r-l)/2)
            merge(arr, l, m, r)
            l += s_size
            if l + s_size-1 < n:
                r = l + s_size - 1
            else:
                r = n-1
        if s_size*2 >= n and not last:
            last = True
            s_size = n
        else:
            s_size = s_size * 2


arr = [7, 6, 5, 4, 3, 2]
#arr = [4, 7, 3, 5, 1]
#arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print(arr)
