"""
@github: github.com/alikhalilli

Time Complexity:
Space Complexity:


[4, 7, 3, 5, 1]
mergeSort(l, m) -> mergeSort(l, m) -> mergeSort(l, m)
                                   -> mergeSort(m+1, r)
                -> mergeSort(m+1, r) -> 
mergeSort(m+1, r) -> mergeSort(m+1, r) -> mergeSort()
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


def mergeSort(arr, l, r):
    if l < r:
        m = int(l + (r-l)/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
