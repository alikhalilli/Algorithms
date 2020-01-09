"""
|1|2|3|4|
"""


def merge(arr, l, m, r):
    i1 = l
    i2 = m + 1
    sortedArr = [None] * (r - l + 1)
    k = 0
    while i1 <= m and i2 <= r:
        if arr[i1] <= arr[i2]:
            sortedArr[k] = arr[i1]
            i1 += 1
        else:
            sortedArr[k] = arr[i2]
            i2 += 1
        k += 1

    while i1 <= m:
        sortedArr[k] = arr[i1]
        i1 += 1
        k += 1

    while i2 <= r:
        sortedArr[k] = arr[i2]
        i2 += 1
        k += 1

    for t in range(k):
        arr[l] = sortedArr[t]
        l+=1


def mergeSort(arr, l, r):
    if l < r:
        m = int(l + (r-l)/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


arr = [4, 7, 3, 5, 1]
mergeSort(arr, 0, len(arr)-1)
print(arr)
